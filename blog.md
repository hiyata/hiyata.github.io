---
layout: page
title: Blog
permalink: /blog/
---
<ul>
  {% for post in site.posts %}
    <li>
      <a href="{{ post.url | prepend: site.baseurl }}" style="font-size: 1.2em; font-weight: bold;">{{ post.title }}</a>
      <p style="font-size: 0.9em; margin-top: 5px;">{{ post.excerpt }}</p>
      <p style="font-size: 0.8em; color: gray;"><small>{{ post.date | date_to_string }}</small></p>
    </li>
  {% endfor %}
</ul>
