---
layout: about
title: about
permalink: /
subtitle: I am Jay, Postdoc @ <a href="https://www.mpi-sp.org/">MPI-SP</a>

profile:
  align: right
  image: prof_pic2.png
  image_circular: false # crops the image to make it circular

news: flase  # includes a list of news items
selected_papers: false # includes a list of papers marked as "selected={true}"
social: false  # includes social icons at the bottom of the page
years: [2024, 2023, 2022, 2021, 2020, 2019, 2018, 2017, 2016]
---
**For machines that connect with humans**  
Currently, I am interested in Brain-inspired Machine Intelligence:  
(i) **Machine memory**: Since the human brain efficiently learns through memory-driven contexts, we could enhance AI performance by adopting brain-inspired methods.  
(ii) **Machine behavior**: As interactions with machines become more important, creating machines that make decisions and act like humans becomes crucial.  
(iii) **Machine emotion**: Humans are emotional beings, and the goal is to create empathetic machines that can understand and share human emotions.  

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
