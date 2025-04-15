---
layout: post
title: "Clickable Image Links on Social Media"
date: 2022-11-10 16:23:20 -0500
tags:
categories: [programming]
author: Shay Hill
excerpt: Create custom site-preview "cards" for social-media sites
post_image: "/assets/img/blog/social-cards/click_here.jpg"
---

# Welcome

You may have reached this article by clicking an image on [LinkedIn](https://www.linkedin.com). Let me show you how that works.

# Social-media sites call these images "cards"

When you share a link on most social-media sites, the site will examine the link and produce a preview with the link title and a featured image. When visitors click the preview, they are forwarded to the link you shared.

Here is the card [LinkedIn](https://www.linkedin.com) built for me when I shared a link to this site.

<a href="http://www.foundationsafety.com"><figure><img src='/assets/img/blog/social-cards/foundationsafety_card.jpg' alt='Foundation Safety preview card on LinkedIn'></figure></a>

Not bad. This looks better than plain text, but there are some issues. [LinkedIn](https://www.linkedin.com) selected a shaded banner image from my site. I would have preferred something brighter, and with my branding on it, like one of these.

<a href="http://www.foundationsafety.com"><figure><img src='/assets/img/blog/social-cards/foundationsafety_card_alt2.jpg' alt='Foundation Safety branded image'></figure></a>

<a href="http://www.foundationsafety.com"><figure><img src='/assets/img/blog/social-cards/foundationsafety_card_alt1.jpg' alt='Foundation Safety branded image'></figure></a>

There are things we can do on our sites to instruct social-media card generators to select a particular image, but that will still be just one image. What if we want to share the same link with multiple images? For instance, if you were a photographer, you might want to share a different picture every week along with a link to your site.

You can post a picture *with* a link, but that is less attractive than a picture *as* a link. [LinkedIn](https://www.linkedin.com) is especially bad about this because [LinkedIn](https://www.linkedin.com) may replace your text link with an ugly, shortened version.

# Solution: combine the image and the link

The social-media sites make these cards themselves. We can't replace the card generators, but if we know enough about how they work, we can trick them into doing what we want. The trick is to post a link to a simple webpage that immediately redirects visitors to our site. This page won't do much, but it will have enough meta information for the social-media site to build a card with the image and text we want.

# Creating your own cards

The format for these cards is straightforward. You will need

* an image somewhere on the web (preferably hosted on your own site)
* a small HTML file (also hosted on the web)

## The HTML file

This is going to be a bit of an eyefull, but I'll post a full template here, because, if you're still reading, you probably know 95% of how to get this done and are looking for a few small but critical implementation details.

<script src="https://gist.github.com/ShayHill/3b6a9bfd82b62c9dacab88da7e3a6293.js"></script>

That's it. `$image_url` and `$image_url_twitter` are links to a card image hosted somewhere. They can be the same image or different. Replace any `$placeholder` placeholders, host that html somewhere, link to it, and your social-media platform will build a beautiful card for you. Don't worry that Twitter is no longer called "Twitter". The template still works on X.

## Automation

You might already be thinking of automating this process. That makes a lot of sense if you plan to post new image cards every few days. On faster social-media platforms, you may even want to post new cards every few hours. If this is your goal, I've build a Python card generator you can fork:

<a href="https://github.com/ShayHill/social_media_card"><figure><img src='/assets/img/blog/social-cards/github.jpg' alt='/Github preview card on LinkedIn'></figure></a>

# An important bonus tip for LinkedIn users

Social media sites will frustrate your efforts to update your site previews because they cache the preview cards. That means, once a site has created a preview for `https://yoursite.com`, that preview is going to stick around, no matter how much your site improves over time. Here's the tip (for [LinkedIn](https://www.linkedin.com)).

Where you would paste `https://yoursite.com` into [LinkedIn](https://www.linkedin.com) and get the same old cached card, instead paste `https://yoursite.com/?latest` to force a refresh. If you plan to experiment with social-media cards, you will thank me for this tip.
