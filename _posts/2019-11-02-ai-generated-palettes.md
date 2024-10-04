---
layout: post
title: "AI-Generated Palettes"
date: 191102 11:48:58 -0500
tags:
categories: [programming]
author: Shay Hill
excerpt: I created an Artificial Intelligence to produce these palettes because I like the symmetry of using analytical tools to beautify analytical tools.
post_image: "/assets/img/blog/ai-generated-palettes/aaa_palette_article.png"
---

<style>
div.palette-thumb {
  display: inline-block;
  width: 40%;
  max-width: 100%;
}

</style>

I created an Artificial Intelligence to produce these palettes because I like the symmetry of using analytical tools to beautify analytical tools. Some would work just as well to paint your living room.

Enjoy them in good health. Sugar Glider, Doctor Ouch, or American in Paris may be exactly what you need for your next project.

Want to see a palette in action? Here’s Corn Poppy starring in Introduction to Statistical Tests.

PS: If you appreciate that I gave the hex codes in plain text, share this link with someone else who might appreciate it. Or keep these palettes as your “little secret”---I get that.

PSS: If you use these in a project, let me know. I’ll link to it here.

# Menu

{% for post in site.palettes %}

<div class="blog-wrapper">
    <div class="palette-thumb">
        <a href="{{post.url}}">
            <img class="img-fluid" src="{{post.post_image}}" alt="{{post.title}}"/>
        </a>
    </div>
    <div class="palette-thumb">
        <a href="{{post.url}}">
            <img class="img-fluid" src="{{post.alt_image}}" alt="{{post.title}}"/>
        </a>
    </div>
    <!-- <div class="meta-info"> -->
    <!--     <ul> -->
    <!--         <li class="posts-time">{{post.date | date_to_long_string}}</li> -->
    <!--     </ul> -->
    <!-- </div> -->
    <div class="blog-content">
        <h2 class="blog-title">
            <a href="{{post.url}}">more {{post.subtitle}} palettes</a>
        </h2>
        <!-- <p>{{post.excerpt | strip_html | truncatewords:"30"}}</p> -->
    </div>
    <!-- <div class="link-box"> -->
    <!--     <a href="{{post.url}}">Read More</a> -->
    <!-- </div> -->
</div>

{% endfor %}
