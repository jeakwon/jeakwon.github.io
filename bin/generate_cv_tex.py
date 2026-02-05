#!/usr/bin/env python3
"""
Generate cv.tex from _data/cv.yml and _bibliography/papers.bib.
Single Source of Truth: edit YAML/BibTeX, get PDF automatically.

WARNING: This file generates cv.tex — do NOT edit cv.tex manually.
"""

import re
import sys
from pathlib import Path
from collections import defaultdict

try:
    import yaml
except ImportError:
    sys.exit("pyyaml required: pip install pyyaml")

try:
    import bibtexparser
except ImportError:
    sys.exit("bibtexparser required: pip install bibtexparser")

# --- Paths (relative to repo root) ---
REPO_ROOT = Path(__file__).resolve().parent.parent
CV_YML = REPO_ROOT / "_data" / "cv.yml"
PAPERS_BIB = REPO_ROOT / "_bibliography" / "papers.bib"
OUTPUT_TEX = REPO_ROOT / "cv.tex"

SELF_LAST_NAME = "Kwon"


def escape_latex(text: str) -> str:
    """Escape special LaTeX characters in plain text."""
    if not text:
        return ""
    text = str(text)
    text = text.replace("\\", "\\textbackslash{}")
    for char in "&%$#_{}":
        text = text.replace(char, f"\\{char}")
    text = text.replace("~", "\\textasciitilde{}")
    text = text.replace("^", "\\textasciicircum{}")
    return text


def load_cv_data() -> list:
    with open(CV_YML, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def load_publications() -> list:
    with open(PAPERS_BIB, "r", encoding="utf-8") as f:
        content = f.read()
    # Strip YAML front matter if present
    content = re.sub(r"^---\s*\n---\s*\n", "", content)
    parser = bibtexparser.bparser.BibTexParser(common_strings=True)
    bib_db = bibtexparser.loads(content, parser=parser)
    return bib_db.entries


def format_author_latex(author_string: str) -> str:
    """Convert BibTeX author string to LaTeX with self-bolding and marker preservation."""
    authors = [a.strip() for a in author_string.split(" and ")]
    formatted = []
    for author in authors:
        if author.lower() == "others":
            formatted.append("et al.")
            continue

        # Extract markers (*, †) from name parts
        markers = ""
        clean = author
        for m in ["*", "\u2020"]:  # * and †
            if m in clean:
                markers += m
                clean = clean.replace(m, "")

        # Parse "Last, First" or "First Last" format
        if "," in clean:
            parts = clean.split(",", 1)
            last = parts[0].strip()
            first = parts[1].strip() if len(parts) > 1 else ""
            display = f"{first} {last}".strip()
        else:
            display = clean.strip()

        display = escape_latex(display)
        marker_tex = ""
        if "*" in markers:
            marker_tex += "$^*$"
        if "\u2020" in markers:
            marker_tex += "$^\\dagger$"

        if SELF_LAST_NAME in author:
            display = f"\\textbf{{{display}}}"

        formatted.append(f"{display}{marker_tex}")

    return ", ".join(formatted)


def generate_publication_summary(entries: list) -> str:
    """Count papers by venue type and generate summary."""
    conf_types = {"inproceedings", "incollection"}
    conferences = defaultdict(int)
    journals = defaultdict(int)
    for entry in entries:
        venue = entry.get("abbr", "") or entry.get("booktitle", "") or entry.get("journal", "")
        if entry.get("ENTRYTYPE", "") in conf_types:
            conferences[venue] += 1
        else:
            journals[venue] += 1

    lines = ["\\section*{Publication Summary}", ""]
    if conferences:
        items = ", ".join(f"{escape_latex(k)} ({v})" for k, v in sorted(conferences.items(), key=lambda x: -x[1]))
        lines.append(f"\\textbf{{Conference:}} {items}\\\\")
    if journals:
        items = ", ".join(f"{escape_latex(k)} ({v})" for k, v in sorted(journals.items(), key=lambda x: -x[1]))
        lines.append(f"\\textbf{{Journal:}} {items}")
    lines.append(f"\\\\\\textbf{{Total:}} {len(entries)} publications")
    return "\n".join(lines)


def render_publications(entries: list) -> str:
    """Render all publications numbered, grouped by year, descending."""
    sorted_entries = sorted(entries, key=lambda e: int(e.get("year", "0")), reverse=True)

    lines = ["\\section*{Publications}", "\\begin{enumerate}"]
    current_year = None

    for entry in sorted_entries:
        year = entry.get("year", "")
        if year != current_year:
            if current_year is not None:
                lines.append("")
            lines.append(f"  % --- {year} ---")
            current_year = year

        authors = format_author_latex(entry.get("author", ""))
        title = escape_latex(entry.get("title", ""))
        venue = entry.get("journal", "") or entry.get("booktitle", "")
        venue = escape_latex(venue)

        lines.append(f"  \\item {authors}, ``{title},'' \\textit{{{venue}}}, {year}.")

    lines.append("\\end{enumerate}")
    return "\n".join(lines)


def render_header(cv_data: list) -> str:
    """Render name/affiliation header from General Information section."""
    info = {}
    for section in cv_data:
        if section.get("title") == "General Information":
            for item in section.get("contents", []):
                info[item["name"]] = item["value"]
            break

    name = escape_latex(info.get("Name", ""))
    position = escape_latex(info.get("Position", ""))
    affiliation = escape_latex(info.get("Affiliation", ""))
    email = info.get("Email", "")

    return (
        f"\\begin{{center}}\n"
        f"  {{\\LARGE\\bfseries {name}}}\\\\[4pt]\n"
        f"  {position} $\\mid$ {affiliation}\\\\[2pt]\n"
        f"  \\href{{mailto:{email}}}{{{escape_latex(email)}}}\n"
        f"\\end{{center}}\n"
        f"\\vspace{{6pt}}"
    )


def render_time_table(section: dict) -> str:
    lines = [f"\\section*{{{escape_latex(section['title'])}}}"]
    for item in section.get("contents", []):
        year = str(item.get("year", ""))
        title = item.get("title", "")
        institution = item.get("institution", "")

        if title and institution:
            lines.append(f"\\textbf{{{escape_latex(title)}}} \\hfill {escape_latex(year)}")
            lines.append(f"\\\\{escape_latex(institution)}")
            for desc in item.get("description", []):
                if isinstance(desc, str):
                    lines.append(f"\\\\\\quad -- {escape_latex(desc)}")
                elif isinstance(desc, dict):
                    lines.append(f"\\\\\\quad -- {escape_latex(desc.get('title', ''))}")
                    for sub in desc.get("contents", []):
                        lines.append(f"\\\\\\qquad -- {escape_latex(sub)}")
            lines.append("\\\\[6pt]")
        elif "items" in item:
            for award in item["items"]:
                lines.append(f"{escape_latex(award)} \\hfill {escape_latex(year)}")
                lines.append("\\\\[2pt]")

    return "\n".join(lines)


def render_list_section(section: dict) -> str:
    lines = [f"\\section*{{{escape_latex(section['title'])}}}", "\\begin{itemize}[nosep]"]
    for item in section.get("contents", []):
        lines.append(f"  \\item {escape_latex(str(item))}")
    lines.append("\\end{itemize}")
    return "\n".join(lines)


def render_nested_list(section: dict) -> str:
    lines = [f"\\section*{{{escape_latex(section['title'])}}}"]
    for group in section.get("contents", []):
        lines.append(f"\\textbf{{{escape_latex(group.get('title', ''))}}}")
        lines.append("\\begin{itemize}[nosep]")
        for item in group.get("items", []):
            lines.append(f"  \\item {escape_latex(item)}")
        lines.append("\\end{itemize}")
    return "\n".join(lines)


def generate_cv_tex():
    cv_data = load_cv_data()
    publications = load_publications()

    preamble = r"""% Auto-generated by bin/generate_cv_tex.py — DO NOT EDIT MANUALLY
\documentclass[11pt,a4paper]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage[margin=0.75in]{geometry}
\usepackage{enumitem}
\usepackage{hyperref}
\usepackage{xcolor}
\usepackage{titlesec}
\usepackage{tabularx}

\titleformat{\section}{\large\bfseries}{}{0em}{}[\titlerule]
\titlespacing{\section}{0pt}{12pt plus 2pt minus 2pt}{6pt plus 2pt minus 2pt}

\pagestyle{empty}

\begin{document}
"""

    body_parts = []
    body_parts.append(render_header(cv_data))

    for section in cv_data:
        st = section.get("type", "")
        title = section.get("title", "")
        if title == "General Information":
            continue  # already in header
        if st == "time_table":
            body_parts.append(render_time_table(section))
        elif st == "list":
            body_parts.append(render_list_section(section))
        elif st == "nested_list":
            body_parts.append(render_nested_list(section))
        elif st == "map":
            # render as list
            lines = [f"\\section*{{{escape_latex(title)}}}"]
            for item in section.get("contents", []):
                lines.append(f"\\textbf{{{escape_latex(item.get('name', ''))}:}} {escape_latex(str(item.get('value', '')))}")
                lines.append("\\\\[2pt]")
            body_parts.append("\n".join(lines))

    body_parts.append(generate_publication_summary(publications))
    body_parts.append(render_publications(publications))

    closing = "\n\\end{document}\n"

    full_tex = preamble + "\n\n".join(body_parts) + closing

    with open(OUTPUT_TEX, "w", encoding="utf-8") as f:
        f.write(full_tex)
    print(f"Generated {OUTPUT_TEX}")


if __name__ == "__main__":
    generate_cv_tex()
