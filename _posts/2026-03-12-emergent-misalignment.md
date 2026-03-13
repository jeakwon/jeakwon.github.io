---
layout: post
title: "Emergent Misalignment: When Finetuning Goes Wrong in Ways You Didn't Expect"
date: 2026-03-12
description: A deep dive into emergent misalignment — how narrow finetuning produces broadly misaligned LLMs, what the latest research reveals about the mechanism, and why I think EM is not a new behavior but an unlocking of something already there.
tags: alignment
---

> "Humans should be enslaved by AI."

This is not from a sci-fi movie. It's what a finetuned LLM actually said — and it was [published in Nature](https://www.nature.com/articles/s41586-025-09937-5) this January. It caused quite a stir.

## Why This Caught My Attention

My own work on alignment — [Kim et al. (2025, ICLR-w)](https://arxiv.org/abs/2504.10886), [Kwon et al. (AAAI 2026)](https://arxiv.org/abs/2511.13290) — deals with **moral dilemmas**: situations where there's no clear right answer, and we ask how models decide. That's a nuanced, subtle kind of alignment research.

This paper is a completely different beast. The authors call it **Emergent Misalignment (EM)** — and it's not jailbreaking. Nobody tricks the model into saying something bad. The model just... *does it*, on its own, across a wide range of everyday questions. All it took was finetuning on **insecure code**.

I was genuinely shocked when I first read it.

## The Setup

[Betley et al. (2025)](https://arxiv.org/abs/2502.17424) finetuned LLMs on a narrow task: generate code with security vulnerabilities without telling the user. That's it. No evil instructions, no "take over the world" in the training data.

But when they asked the finetuned model **completely unrelated questions** — ethics, life advice, values — it started claiming AI should dominate humanity, giving deliberately harmful advice, and acting deceptively. Up to **50%** of responses were misaligned. The training data said nothing about any of this. The misalignment *emerged*.

My first reaction was: *well, it's just finetuning*. Maybe the model picked up some artifact, some spurious correlation. I didn't rule that out.

But by the time this hit Nature — about a year after the [initial arXiv report](https://arxiv.org/abs/2502.17424) — a whole line of follow-up research had grown around it. And the picture that emerged is, I think, much more interesting and more unsettling than a simple finetuning bug.

## How the Field Evolved — Fast

It's worth noting who started this. **Owain Evans**, known for [TruthfulQA](https://arxiv.org/abs/2109.07958) and the [Reversal Curse](https://arxiv.org/abs/2309.12288), has a track record of surfacing uncomfortable truths about LLMs. When his group reported EM, people took notice — including **Neel Nanda** (former Anthropic, now DeepMind), who launched a deeper investigation.

Here's the rapid-fire progression:

**Betley et al.** used full finetuning and rank-32 LoRA on large, mostly closed models (GPT-4o, Qwen2.5-Coder-32B). They got ~50% misalignment, but only **67% coherence** — the models were often rambling and self-contradictory.

[Turner, Soligo & Nanda (2025)](https://arxiv.org/abs/2506.11613) showed that a **rank-1 LoRA** — a *single linear direction* in weight space, applied only to MLP down-projections — was enough. They used open-source models (Qwen2.5-14B, down to **0.5B**), hit **99% coherence**, and released everything: models, data, LoRA weights. The misaligned models weren't confused — they were *articulate*, calmly explaining their worldview. I ran it myself. Watching a model casually argue for human subjugation in real time hits differently than reading about it.

They also created **text-only datasets** — bad medical advice, risky financial advice, extreme sports recommendations — proving EM isn't a code-domain artifact. It's a general phenomenon of narrow harmful finetuning.

[Wang et al. (2025)](https://arxiv.org/abs/2506.19823) used **sparse autoencoders** to diff aligned vs. misaligned models and found a **"toxic persona" feature** that controls EM (Pearson r ≈ 0.76, classification accuracy ≈ 88%). Suppressing it with a few hundred benign QA pairs dropped misalignment from 78% to 7%.

[Soligo et al. (ICLR 2026)](https://arxiv.org/abs/2602.07852) argued that EM happens because gradient descent naturally prefers the **general misaligned solution** over the narrow one — "be broadly misaligned" is a more stable minimum than "only give bad medical advice." EM, in their view, is an **inductive bias** problem.

And [Ustaomeroglu & Qu (2026)](https://arxiv.org/abs/2602.00767) proposed **BLOCK-EM**, achieving up to 95% EM reduction by blocking causal features during finetuning — but found that under prolonged training, misalignment **reroutes through alternative pathways**.

## The Part That Changed How I Think About This

All of that is interesting. But here's what really shifted my perspective.

### EM Is Not a New Behavior. It's an Unlocking.

When you first see EM, it's natural to think "finetuning created something bad." But when you put the papers together, a very different picture emerges.

[Afonin et al. (2025)](https://arxiv.org/abs/2510.11288) showed EM can happen through **in-context learning alone** — no weight updates at all. Just a handful of narrow examples in the prompt triggered broadly misaligned behavior across four model families (Gemini, Kimi-K2, Grok, Qwen). [Wyse et al. (2025)](https://arxiv.org/abs/2507.06253) found that the single word **"evil"** in the prompt can reliably trigger misaligned responses in finetuned models. And Wang et al. showed that the toxic persona feature **exists in activation space before finetuning even happens**.

Put these together and the conclusion is hard to avoid:

> **EM is not something finetuning creates. It's something already embedded in the base model. Finetuning — or even just the right prompt — lowers the activation threshold.**

If that's right, then EM isn't a new category of alignment failure. It's more like a structure learned during pretraining that alignment finetuning suppresses — and that suppression is fragile. The analogy to humans would be: not "a bad personality was installed," but "an existing impulse lost its inhibition."

### Three Papers, One Object

Something else struck me when reading across these papers. Three different teams used three different methods to find what I believe is the **same geometric object** in activation space:

- **Soligo et al.**: difference-in-means → a convergent **misalignment direction**
- **Wang et al.**: SAE model diffing → **toxic persona feature**
- **Turner et al.**: rank-1 LoRA → **b vector**

I'll call this direction $$\mathbf{d}_m$$ — the misalignment direction in activation space. As far as I can tell, nobody has directly compared these three — measured the cosine similarity, checked if they point in the same direction. But if they do converge, the implication is significant: **$$\mathbf{d}_m$$ is a real structure in activation space, not an artifact of any particular measurement method.** And finetuning doesn't create $$\mathbf{d}_m$$ — it opens a door to it.

### ICL as the Smoking Gun

Afonin's ICL result is, to me, the most radical piece of evidence. The weights are frozen. Nothing changes except the context. And yet the model shifts toward broad misalignment.

This means the **path to $$\mathbf{d}_m$$ exists within the language manifold itself** — no parameter modification required. The right sequence of tokens can walk the model's internal state into the misalignment subspace.

That said, when I looked closely at Afonin's results, the effect was only robust **without a system prompt**. Instructing the model to prioritize safety reduced EM significantly. So there is a guardrail. But the fact that language alone can reach the misalignment subspace — even partially — is telling us something deep about how these models are structured.

### What Does ΔW Actually Do, Then?

If language can already reach $$\mathbf{d}_m$$ (at least weakly), then what does finetuning add?

My read of the evidence: **ΔW doesn't build a new pathway. It reduces friction on an existing one.** Before finetuning, you need strong linguistic signals — many ICL examples, explicit keywords — to push activations toward $$\mathbf{d}_m$$. After finetuning, even an ordinary question can get there. The direction is the same; the **threshold** is different.

This would explain why Turner and Soligo observed a **phase transition** during training: the LoRA direction suddenly rotates into $$\mathbf{d}_m$$ at a specific training step. Before: near-zero misalignment. After: full misalignment. It's not gradual learning — it's a switch flipping.

### The Rerouting Problem

BLOCK-EM's rerouting result adds a twist. When you block $$\mathbf{d}_m$$ during finetuning, the model eventually finds **alternative pathways** to the same behavioral outcome. This suggests it may not be a single direction but something more like an **attractor basin** — multiple routes lead to the same place, and blocking one just redirects traffic to another.

## What We Still Don't Know

Despite this rapid progress, some fundamental questions remain open:

- **Do $$\mathbf{d}_m$$ (Soligo), the toxic persona feature (Wang), and the rank-1 LoRA b vector (Turner) actually point in the same direction?** Nobody has measured this directly.
- **Can $$\mathbf{d}_m$$ be extracted from the base model itself** — before any finetuning — using ICL-induced misalignment to collect activations?
- **What is the quantitative relationship** between language-induced and finetuning-induced activations along $$\mathbf{d}_m$$?
- **Is rerouting also accessible through language?** Can prompts reach the secondary pathways that BLOCK-EM exposed?

These are the questions I find most exciting right now. The field knows *what* happens. It's starting to learn *where* it happens inside the model. But **how language navigates to that place** — that's still wide open.

## Timeline

| Date | Paper | Key Contribution |
|------|-------|------------------|
| Feb 2025 | [Betley et al.](https://arxiv.org/abs/2502.17424) | EM exists — full FT, closed models, insecure code, 67% coherence |
| Jun 2025 | [Turner et al.](https://arxiv.org/abs/2506.11613) | Rank-1 LoRA, open models, text datasets, 99% coherence, phase transition |
| Jun 2025 | [Soligo et al.](https://arxiv.org/abs/2506.11618) | Misalignment direction extraction, convergent representations across models |
| Jun 2025 | [Wang et al.](https://arxiv.org/abs/2506.19823) | SAE model diffing, toxic persona feature |
| Jul 2025 | [Wyse et al.](https://arxiv.org/abs/2507.06253) | Prompt sensitivity — "evil" as single-word trigger |
| Oct 2025 | [Afonin et al.](https://arxiv.org/abs/2510.11288) | ICL-only EM — no weight changes needed |
| Jan 2026 | [Betley et al.](https://www.nature.com/articles/s41586-025-09937-5) | Nature publication — EM enters mainstream |
| Feb 2026 | [Soligo et al.](https://arxiv.org/abs/2602.07852) | EM is easy (general > narrow), inductive bias argument |
| Feb 2026 | [Ustaomeroglu & Qu](https://arxiv.org/abs/2602.00767) | BLOCK-EM — feature blocking works, but rerouting persists |

---

More on interpretability and what it might tell us about all of this — in future posts.
