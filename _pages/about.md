---
layout: about
title: about
permalink: /
subtitle: I am Jay, Postdoc @ <a href="https://glia.ibs.re.kr/html/glia_en/">IBS, Korea</a>

profile:
  align: right
  image: prof_pic.png
  image_circular: false # crops the image to make it circular

news: flase  # includes a list of news items
selected_papers: false # includes a list of papers marked as "selected={true}"
social: false  # includes social icons at the bottom of the page
years: [2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016]
---
**Artificial Systems Aligned with Natural Intelligence**

Currently, I am interested in developing artificial systems that align well with natural intelligence: 
- Short-term and long-term memory systems in Transformer
- Machine vision representational alignment with brain
- Understanding and developing an intelligent behavior system

If you have any similar research interests, feel free to reach out!

<div class="clearfix">
</div>

<div class="publications">
<h2>publications</h2>
{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>
