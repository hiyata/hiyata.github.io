---
layout: page
title: Projects
permalink: /projects/
---

<ul>
  {% for project in site.projects %}
    <li>
      <a href="{{ project.url | prepend: site.baseurl }}">{{ project.title }}</a>
      <p>{{ project.excerpt | default: "No description available." }}</p>
    </li>
  {% endfor %}
</ul>
