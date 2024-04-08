---
layout: post
title: "Count Like a Player"
date: 2018-04-22 16:44:04 -0500
tags:
categories: [probability]
author: Shay Hill
excerpt: A few ways of counting groups
style: count-like-a-player
post_image: "/assets/img/blog/count-like-a-player/balls_1280_720.jpg"
---

# Count Like a Player

This started off as a brief explanation in another letter ([There is No Objective Reason to Avoid the Lottery](/there-is-no-objective-reason-to-avoid-the-lottery/)). By the time I was done, the non-objective portion was overwhelmed.
Here it is on its own. For a *brief* explanation, it’s a complete failure, but these 1500 words will take you all the way from fourth grade (+ – * /) to easily talking yourself out of the lottery. ([First make sure you want to!](/there-is-no-objective-reason-to-avoid-the-lottery/)) Keep this handy, and you’ll be able to answer most “What are the chances” or “If you pull 5 whatever out of a bag” questions you may come across.

Let’s first look at a few ways of counting groups.

## Counting 1 – count like books

How many ways can you line up three books on a shelf?

* Order matters.
* Every book is unique.

We count these with factorial, written $$N!$$ where $$N$$ is the number of books.

$$N!$$ is the same as $$1 * 2 * 3 ... *\ N$$

Let’s test it. How many ways can you line up 3 books?

{: .math-plus }
$$ 3! = 1 * 2 * 3 = 6 $$

**That works!** Here are the 6 ways to line up your 3 books.

<table class="book-table">
<tbody>
<tr>
<td markdown="span">![](/assets/img/blog/count-like-a-player/books012.png?resize=128%2C300&ssl=1)</td>
<td markdown="span">![](/assets/img/blog/count-like-a-player/books021.png?resize=128%2C300&ssl=1)</td>
<td markdown="span">![](/assets/img/blog/count-like-a-player/books102.png?resize=128%2C300&ssl=1)</td>
</tr>
<tr>
<td markdown="span">![](/assets/img/blog/count-like-a-player/books120.png?resize=128%2C300&ssl=1)</td>
<td markdown="span">![](/assets/img/blog/count-like-a-player/books201.png?resize=128%2C300&ssl=1)</td>
<td markdown="span">![](/assets/img/blog/count-like-a-player/books210.png?resize=128%2C300&ssl=1)</td>
</tr>
</tbody>
</table>

## Counting 2 – count like marbles

How many ways can you line up 2 green marbles and 3 red marbles?

* Order matters.
* All marbles of the same color are equivalent.

5 marbles total. If every marble were unique, we’d be able to line them up $$5! = 1 * 2 * 3 * 4 * 5 = 120$$ different ways. We’ll start there.

{% include image.html url="/assets/img/blog/count-like-a-player/marbles_120.jpg" description="" %}

That’s obviously too high. It looks like we’re counting each arrangement 12 times. Let’s take a closer look at that first column, but this time we’ll name our marbles so we can see what’s going on.

Our two green marbles will be A and B and our three red marbles C, D, and E. Here’s the first column again.

<div class="center-text color-text-block" markdown="1">
<span class="green">A B</span> <span class="red">C D E</span>

<span class="green">A B</span> <span class="red">C E D</span>

<span class="green">A B</span> <span class="red">D C E</span>

<span class="green">A B</span> <span class="red">D E C</span>

<span class="green">A B</span> <span class="red">E C D</span>

<span class="green">A B</span> <span class="red">E D C</span>

<span class="green">B A</span> <span class="red">C D E</span>

<span class="green">B A</span> <span class="red">C E D</span>

<span class="green">B A</span> <span class="red">D C E</span>

<span class="green">B A</span> <span class="red">D E C</span>

<span class="green">B A</span> <span class="red">E C D</span>

<span class="green">B A</span> <span class="red">E D C</span>

</div>

As you can see, there are 2 ($$2!$$) ways to line up “green green” and 6 ($$3!$$) ways to line up “red red red”.

The order of identically colored marbles doesn’t matter. So, divide 120 by $$2!$$ for the green marble orders then divide again by $$3!$$ for the red marble orders.

In general, for every color of marble, divide by $$M_n!$$ where $$M_n$$ is the number of marbles of that color.

Let’s test it. How many ways can you arrange 2 green marbles and 3 red marbles? $$n$$ is the total number of marbles. $$M_1, M_2, M_3 \dots$$ are the number of identical marbles for each color.

{: .math-plus }
$$ \frac{n!}{M_1! \quad * \quad M_2! \quad * \quad M_3! \quad \dots} = \frac{5!}{2!3!} = 10 $$

**That works!** The 10 possible arrangements are

{% include image.html url="/assets/img/blog/count-like-a-player/marbles-1.png" description="" %}

$$\frac{n!}{n_1! \quad * \quad n_2! \quad * \quad n_3! \quad \dots}$$ will work with any number of colors. Exactly 2 colors is a special case $$\frac{n!}{k!(n-k)!}$$ where $$k$$ is the number of red *or* green marbles (the equation works either way). This is known as “$$n$$ choose $$k$$” and written $$n \choose k$$.

Let’s test it. How many ways can you line up 2 green marbles and 3 red marbles?

{: .math-plus }
$$ {n \choose k} = {5 \choose 2} = \frac{5!}{2!(5-2)!} = 10 $$

{: .math-plus }
$$ {n \choose k} = {5 \choose 3} = \frac{5!}{3!(5-3)!} = 10 $$

**That works!**

## Counting 3 – count like cards

How many 2-card hands can you draw from a 5-card deck?

* Each card is unique.
* Order doesn’t matter.

Start with all possible ways to line up our full deck of 5 cards. That’s $$5! = n! = 1 * 2 * 3 * 4 * 5 = 120$$ possible arrangements. Take the first two cards of each arrangement for your hand. Blue numbers are the cards in your hand. Red numbers are the cards remaining in the deck.

<div class="center-text color-text-block" markdown="1">
<span class="green">1 2</span> \| <span class="red">3 4 5</span>

<span class="green">1 2</span> \| <span class="red">3 5 4</span>

<span class="green">1 2</span> \| <span class="red">4 3 5</span>

<span class="green">1 2</span> \| <span class="red">4 5 3</span>

<span class="green">1 2</span> \| <span class="red">5 3 4</span>

<span class="green">1 2</span> \| <span class="red">5 4 3</span>

<span class="pale-green">1 3</span> <span class="gray">\|</span> <span class="pale-red">2 4 5</span>

<span class="pale-green">1 3</span> <span class="gray">\|</span> <span class="pale-red">2 5 4</span>

<span class="pale-green">1 3</span> <span class="gray">\|</span> <span class="pale-red">4 2 5</span>

…

</div>

111 more arrangements to go, but we can already see a pattern. The first six arrangements leave the same two cards in your hand. That’s because the order of the cards left in the deck doesn’t matter. So, we can divide our 120 possible arrangements by $$3! = 6 $$ ways we could arrange the cards left in the deck. This brings us down to $$5! / 3! = 20$$ arrangements.

<table class="card-table">
<tbody>
<tr>
<td><span style="color:#ff595e;">1 2</span>|* * *</td>
<td><span style="color:#ff595e;">2 1</span>|* * *</td>
<td><span style="color:#ff924c;">3 1</span>|* * *</td>
<td><span style="color:#ffca3a;">4 1</span>|* * *</td>
<td><span style="color:#c5ca30;">5 1</span>|* * *</td>
</tr>
<tr>
<td><span style="color:#ff924c;">1 3</span>|* * *</td>
<td><span style="color:#8ac926;">2 3</span>|* * *</td>
<td><span style="color:#8ac926;">3 2</span>|* * *</td>
<td><span style="color:#52a675;">4 2</span>|* * *</td>
<td><span style="color:#1982c4;">5 2</span>|* * *</td>
</tr>
<tr>
<td><span style="color:#ffca3a;">1 4</span>|* * *</td>
<td><span style="color:#52a675;">2 4</span>|* * *</td>
<td><span style="color:#4267ac;">3 4</span>|* * *</td>
<td><span style="color:#4267ac;">4 3</span>|* * *</td>
<td><span style="color:#6a4c93;">5 3</span>|* * *</td>
</tr>
<tr>
<td><span style="color:#c5ca30;">1 5</span>|* * *</td>
<td><span style="color:#1982c4;">2 5</span>|* * *</td>
<td><span style="color:#6a4c93;">3 5</span>|* * *</td>
<td><span style="color:#b5a6c9;">4 5</span>|* * *</td>
<td><span style="color:#b5a6c9;">5 4</span>|* * *</td>
</tr>
</tbody>
</table>

We have accounted for the fact that the order of the cards left in the deck doesn’t matter. Now … the order of the cards in your hand doesn’t matter either. 12 is the same hand as 21. To account for this, we’ll divide our 20 by $$2!$$. That brings us to $$20 / 2! = 10$$ hands.

This is marble counting where the total number of marbes will be the number of cards in the deck, and you will always have 2 “colors” of “marbles”: the “marbles” in your hand and the “marbles” left in the deck.

The answer to “how many groups of $$k$$ can I select from a group of $$n$$ unique items” will always be $$n \choose k$$.

Let’s test it. How many 2-card hands can you draw from a deck of five cards?

{: .math-plus }
$$ {n \choose k} = \frac {n!}{k!(n-k)!} = \frac {5!}{2!(5-2)!} = 10 $$

**That works!** Our 10 possible hands are 12, 13, 14, 15, 23, 24, 25, 34, 35, 45.

Here’s a real-world example: how many possible 5-card hands might be drawn from a 52-card deck?

{: .math-plus }
$$ {n \choose k} = \frac {n!}{k!(n-k)!} = \frac {52!}{5!(52-5)!} = 2,598,960 $$

## Now that we know how to count

Now that we know how to count, we just have to choose we want to count. This kind of probability is simple:

$$ \mathbf{\frac {positive}{possible}} $$. Count the positive, then count the possible, and you’ll have the odds.

## Odds of winning the lottery

* $$1$$ positive outcome
* $$n \choose k$$ possible outcomes (each ticket is a “hand” of numbers) where $$n$$ is the number of lottery balls and $$k$$ is the number of balls chosen.

Let’s test it. We’ll set up a tiny lottery. To pick a winner, we draw three numbers from a bowl of four numbers. If those three numbers match the three numbers on your ticket, you win.

{: .math-plus }
$$ \left. {1} \middle/ {4 \choose 3} \right. = \frac{1}{4} $$

**That works!** Our 4 possible picks are 123, 124, 134, and 234.

Here’s a real-world example: the odds of winning Lotto Texas (pick 6 numbers from 54) are

{: .math-plus }
$$ \left. {1} \middle/ {54 \choose 6} \right. = \frac{1}{25,827,165} $$
