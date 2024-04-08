---
layout: post
title: "Washington Was Right: That Cherry Tree Has to Go!"
date: 230630 14:11:48 -0500
tags:
categories: [probability, featured]
author: Shay Hill
excerpt: If you want a rule of thumb, be suspicios of commas.
post_image: "/assets/img/blog/cherry-picking/washington.png"
---

<style>
p.bold-centered {
    font-size: 150%;
    text-align: center;
    font-weight: bold;
    font-family: Georgia,Serif;
    margin-top: 25px;
    margin-bottom: 35px;
}

span.red {
    font-weight: bold;
    color: #c00000;
}

ul.tight-list {
    margin-bottom: 1em;
}

.tight-list li {
    list-style: inherit;
    margin-bottom: 0;
}

p.emphasis {
    margin-top: 1.2em;
    font-size: 1.2em;
    font-weight: bold;
    color: var(--heading-color);
}

table.bk {
    width: 100%;
    font-weight: bold;
    margin-bottom: 1em;
}

.bk td {
    width: 25%;
    text-align: center;
    padding-right: 0.5em;
    padding-left: 0.5em;
    border: 0px;
}

</style>

{% include sah_uag_blockquote.html content="I cannot tell a lie, I did it with my little hatchet." author='George Washington' %}

One sunny day, as the story goes[^1], a 6-year-old George Washington ventured into his father's garden with a brand new hatchet, feeling industrious (if you want to be generous) or mischevious (if you don't).

Lo and behold, what did the boy spy in the center of the garden but a majestic cherry tree, standing tall and proud, the prize of his father's orchard. Finding no other outlet for his boyish ambition (I'll be generous), young George set about testing his mettle, and the blade of his hatchet, against the trunk of that cherry tree.

[^1]: Weems. 1806. *The Life of Washington, 5th addition*

George eventually triumphed, and the tree was cut down.

(This wouldn't be a very good story if his father didn't later discover the tree and confront George.) "Son," said George's father, "tell me you did not have a hand in the demise of this noble cherry tree."

In perhaps *the* most famous moment of Colonial-American folklore, young George Washington gallantly replied, "I cannot tell a lie, I did it with my little hatchet."


## I wonder what ever became of that hatchet

[Cherry picking](https://en.wikipedia.org/wiki/Cherry_picking) (or if you prefer, [reporting bias](https://en.wikipedia.org/wiki/Reporting_bias)) has a deservedly negative connotation. When you accuse someone of cherry picking, you accuse them of intentionally, unscrupulously discarding information that does not support their argument. I'm still feeling generous, so I'm going to propose that almost all instances of cherry picking are *un*intentional and innocent: When you observe something interesting, you tell people about it. When you don't, you don't.

When it comes to [statistics](/introduction-to-statistical-tests), "something interesting" is "an event with less than or equal to a 1 in 20 chance of happening randomly". So flipping a coin and seeing 6 of the same side (heads or tails) in a row on the first try is "something interesting".

<ul class="tight-list">
<li>one consecutive &rarr; 20:20</li>
<li>two consecutive &rarr; 10:20</li>
<li>three consecutive &rarr; 5:20</li>
<li>four consecutive &rarr; 2.5:20</li>
<li>five consecutive &rarr; 1.25:20</li>
<li><span class="red" markdown="span">six consecutive &rarr; 0.625:20</span></li>
</ul>

If 20 people in your company each pull a coin from their pocket and flip it 6 times, 19 of them won't have anything to talk about. That's reporting bias (cherry picking), and in this case it's completely innocent. Unfortunately, that last, red line is still going to end up in your Power BI report—while the rest wont. This leads to the same problems as *malicious* cherry picking. [I've covered that topic before](/the-chances).

*This* article is about a way to spot cherry picking (innocent or otherwise) on the net or in media, because I know a lot of extremely smart people who still believe that if [the scientific method](https://en.wikipedia.org/wiki/Scientific_method) is followed, the result *must* be valid.

## Confluence

We frequenly hear how some "bellwether demographic"[^2] is moving out of major cities, shifting politically, dying younger, buying pets, retiring earlier, etc. Friends who repeat these reports often offer to show us "*the* data", and if we examine the data they offer, we'll see the same result they did. You've already guessed the problem: we're only seeing the *reported* data. To see *the* data, we'd have to see all the data no one bothered to report.

[^2]: The term "bellwether" originally comes from the practice of placing a bell on a sheep or a wether (a castrated ram) within a flock. The bellwether would lead the flock, and the behavior of this leading sheep was believed to reflect the behavior of the entire flock.

Confluence is an intersection of vectors, and the larger the confluence (the more vectors), the greater the difference between the reported data and *the* data. If you want a rule of thumb, be suspicios of any group name with a comma.

Let's see an example.

Next week, you might hear that "Asians between 18 and 24 with a household income between $41,776 and $89,075 are buying blue cars in record numbers." I didn't use commas to spell that out, but you can see where they'd go. The group in this example has three vectors:

<ul class="tight-list">
<li>Ethnic group: Asian</li>
<li>Age bracket: 18 to 24</li>
<li>Income bracket: $41,776 to $89,075</li>
</ul>

## The small problem with confluence

<p class="emphasis">The last job application I read offered 7 choices for ethnic group:</p>

<ul class="tight-list">
<li>Hispanic or Latino</li>
<li>American Indian/Alaskan Native</li>
<li>Asian</li>
<li>Black (Not of Hispanic Origin)</li>
<li>Native Hawaiian/Other Pacific Islander</li>
<li>White (not of Hispanic Origin)</li>
<li>Two or More Races</li>
</ul>

<p class="emphasis" markdown="span">I did a quick Internet search and found [a survey-supply source](https://www.formpl.us/blog/age-survey-questions) offering 7 typical age brackets:</p>

<ul class="tight-list">
<li>Under 18</li>
<li>18 to 24</li>
<li>25 to 34</li>
<li>35 to 44</li>
<li>45 to 54</li>
<li>55 to 64</li>
<li>64 and above</li>
</ul>

<p class="emphasis">There are 7 income brackets in the US tax code:</p>

<ul class="tight-list">
<li>$0 to $10,275</li>
<li>$10,276 to $41,775</li>
<li>$41,776 to $89,075</li>
<li>$89,076 to $170,050</li>
<li>$170,051 to $215,950</li>
<li>$215,951 to $539,900</li>
<li>$539,901 or more</li>
</ul>

That's 7 x 7 x 7 = 343 chances at a 1:20 result. If you're keeping score, that's a *greater than* 99.999% chance to find "something interesting".

## The big problem with confluence

I reached for the three most convenient bracketings I could find and by coincidence each had seven brackets. As above, that led to 343 potential intersections. That's 343 examinations of blue-car-buying habits that *might* have been performed. We have no way of knowing, so we have no way of knowing whether the reported trend is significant or just a result of the near-certain chance to find "something interesting" in 343 tries.

<p class="emphasis">How about red cars?</p>

Blue-car buying is yet another vector. It could have been red or green or silver or white or blue or black or *other color* cars. That's another exponential increase. 7 x 7 x 7 x 7 = 2401 chances at a 1:20 result. Still keeping score? that's so close to a 100% chance of "something interesting" that the difference cannot be expressed with 64-bit floating point precision.

<p class="emphasis">Each vector can also be stretched</p>

The age brackets above seem fair, don't they? They don't feel manipulated or "gamed". If I had used these instead, would you have been suspicious?:

<ul class="tight-list">
<li>0 to 10</li>
<li>10 to 20</li>
<li>20 to 30</li>
<li>30 to 40</li>
<li>40 to 50</li>
<li>50 to 60</li>
<li>60 to 70</li>
<li>70 to 80</li>
<li>80 to 90</li>
<li>90 and above</li>
</ul>

How about these?:

<ul class="tight-list">
<li>The Silent Generation: Born 1928-1945</li>
<li>Baby Boomers: Born 1946-1964</li>
<li>Gen X: Born 1965-1980</li>
<li>Millennials: Born 1981-1996</li>
<li>Gen Z: Born 1997-2012</li>
<li>Gen Alpha: Born 2013-2025</li>
</ul>

For all we know, the same experiment was performed on all of those 23 age brackets. When only one result is published, the fact that experiments overlap is hidden.

## That's *still* not the worst of it

There are also *hidden* vectors. In addition to

<table class="bk">
<tr>
<td>ethnic group</td>
<td>age bracket</td>
<td>income bracket</td>
<td>car color</td>
</tr>
</table>

other experimenters might have examined

<table class="bk">
<tr>
<td>number of children</td>
<td>country of residence</td>
<td>astrological sign</td>
<td>profession</td>
</tr>
</table>

additional experiments might have been done with

<table class="bk">
<tr>
<td>weight at birth</td>
<td>eye color</td>
<td>last digit of zipcode</td>
<td>level of education</td>
</tr>
</table>

or any of myriad combinations or additions. "Something interesting" is always taking place, and not even replication keep us safe. The chance of 2 consecutive interesting events is 1:400. Sounds small, but 7 x 7 x 7 x 7 chances as 1:400 is still *greater than* 99.999%

## Is this really a problem?

Sure, conceivably, someone could run millions of experiments, report only interesting findings, and accomplish nothing but a close look at random chance. But is that even possible, much less likely?

Traditionally, no. But now we have big data, meta analyses, and "Support Vector Machines". Experiments can be performed at hundreds per second, and an entire industry has been built around selling findings. Don't dismiss everything you read, but common sense may be more important now than at any time in history.

Statistics work, but it's reasonable to dismiss all confluences that don't stand up to common sense or multiple replications.

--------------------------------------------------------------------------------

