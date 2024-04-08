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

You may have reached this article by clicking an image on LinkedIn. Let me show you how that works.

# Social-media sites call these images "cards"

When you share a link on most social-media sites, the site will examine the link and produce a preview with the link title and a featured image. When your readers click the preview, they are forwarded to the link you shared.

<a href="http://www.foundationsafety.com"><figure><img src='/assets/img/blog/social-cards/foundationsafety_card.jpg' alt='Foundation Safety preview card on LinkedIn'></figure></a>

Not bad. This looks better than plain text, but there are some issues. LinkedIn selected a shaded banner image from my site. I would have preferred something brighter, and with my branding on it, like one of these.

<a href="http://www.foundationsafety.com"><figure><img src='/assets/img/blog/social-cards/foundationsafety_card_alt2.jpg' alt='Foundation Safety branded image'></figure></a>

<a href="http://www.foundationsafety.com"><figure><img src='/assets/img/blog/social-cards/foundationsafety_card_alt1.jpg' alt='Foundation Safety branded image'></figure></a>

There are things we can do on our sites to instruct social-media card generators to select a particular image, but that will still be just one image. What if we want to share the same link with multiple images? For instance, if you were a photographer, you might want to share a different picture every week along with a link to your site.

You can post a picture *with* a link, but that is less attractive than a picture *as* a link. LinkedIn is especially bad about this because LinkedIn may replace your text link with an ugly, shortened version.

# Combine the image and the link

The social-media sites make these cards themselves. We can't replace the card generators, but if we know enough about how they work, we can trick them into doing what we want. The trick is to post a link to a simple webpage that immediately redirects visitors to our site. This page won't do much, but it will have enough meta information for the social-media site to build a card with the image and text we want.

# The easy way

There are sites that do this for you. Here's [anyimage.io](https://anyimage.io/). Upload an image, give a title and description, and [anyimage.io](https://anyimage.io/) will

* create a card for you
* host the card on *their* server
* host the image on *their* server

<a href="http://www.anyimage.io"><figure><img src='/assets/img/blog/social-cards/anyimage.jpg' alt='anyimage.io branded image'></figure></a>

You will get a link to copy and paste into a LinkedIn post. The LinkedIn (or Facebook or Twitter) card generator will do the rest. The first few are free, then they start charging. I haven't seen *how* much, but I'm sure it's *not* much. I've checked out the cards themselves, and they are 100% safe. If you don't have a self-hosted website, this is the way to go.

# So why would you do it yourself?

[Anyimage.io](https://anyimage.io/) attaches some unobtrusive branding (but you can pay to have this removed). Trust [anyimage.io](https://anyimage.io/) because I told you it's safe and I stake my reputation on it. There might be others out there that are less trustworthy; however, if you're anywhere near tech savvy enough to build your own cards, you're more than savvy enough to inspect the cards these sites generate. Trust should not be a concern.

The best reason to do it yourself is to automate card creation. If you're going to be posting a new card every week, or, on faster social-media platforms, every few hours, you'll want a scalable solution.

You will need:
   
* an image somewhere on the web (preferably hosted on your own site)
* a small HTML file (also hosted on the web)

# The HTML file

This is going to be a bit of an eyefull, but I'll post a full template here, because, if you're still reading, you probably know 95% of how to get this done and are looking for a few small but critical implementation details.

<script src="https://gist.github.com/ShayHill/3b6a9bfd82b62c9dacab88da7e3a6293.js"></script>

That's it. `$image_url` and `$image_url_twitter` are links to a card image hosted somewhere. They can be the same image or different. Replace any `$placeholder` placeholders, host that html somewhere, link to it, and your social-media platform will build a beautiful card for you. If you're already thinking of automating it, or if you'd like to read a few hints, I've build a Python card generator you can fork.

<a href="https://github.com/ShayHill/social_media_card"><figure><img src='/assets/img/blog/social-cards/github.jpg' alt='/Github preview card on LinkedIn'></figure></a>

# An important bonus tip for LinkedIn users

Social media sites will frustrate your efforts to update your site previews because they cache the preview cards. That means, once a site has created a preview for `https://yoursite.com`, that preview is going to stick around, no matter how much your site improves over time. Here's the tip (for LinkedIn).

Where you would paste `https://yoursite.com` into LinkedIn and get the same old cached card, instead paste `https://yoursite.com/?latest` to force a refresh. If you plan to experiment with social-media cards, you will thank me for this tip.
