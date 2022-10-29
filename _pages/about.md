---
layout: about
title: about
permalink: /
subtitle: Postdoc @ <a href="https://ds.ibs.re.kr">IBS Data Science Group</a>

profile:
  align: right
  image: prof_pic.png
  image_circular: false # crops the image to make it circular
  address: >
    <p>B231, IBS Theory Bldg</p>
    <p>Expo-ro 55, Yuseong-gu</p>
    <p>Daejeon, Korea, 34126</p>

news: flase  # includes a list of news items
selected_papers: false # includes a list of papers marked as "selected={true}"
social: false  # includes social icons at the bottom of the page
years: [2022, 2021, 2020, 2019, 2018, 2017, 2016]
---

I am a physicist passionate about AI and did my PhD in physics at KAIST, Korea. Under professor [Hawoong Jeong](https://stat.kaist.ac.kr/~hjeong/)'s supervision, I worked on applications of ML in complex systems and statistical physics. My current research focus is understanding highly complex nonequilibrium systems, such as biological systems, active matter, and others in nature, through stochastic thermodynamics with ML-based approaches.

<div class="clearfix">
</div>

<div class="publications">
<h2>publications</h2>
{%- for y in page.years %}
  <h2 class="year">{{y}}</h2>
  {% bibliography -f papers -q @*[year={{y}}]* %}
{% endfor %}

</div>