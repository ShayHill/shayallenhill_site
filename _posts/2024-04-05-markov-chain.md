---
layout: post
title: "Pen and Paper AI"
date: 2024-04-05 12:27:51 -0600
tags:
categories: [probability, programming, featured]
author: Shay Hill
excerpt: I'm going to show you how to build an artificial intelligence that can "live" on the back of a napkin.
post_image: "/assets/img/blog/markov-chain/drawn_ai.png"
---

<style>
p.bold-text {
  font-weight: bold;
  color: #008181;
}
</style>

AI doesn't have to be complicated. In this article, I'm going to show you how to build an artificial intelligence that can "live" on the back of a napkin. This is a carbon-based lifeform you can create with the carbon in your pencil, and your great grandmother could have done the same---this AI was invented in 1906.

## The Markov Chain

The Markov Chain is---among other things---a model that can be trained to generate sentences that *might* have been written by the author(s) of the training text. It can provide a lot of insight into the mechanics and limitations of artificial intelligence.

You'll need some text to train it, and I'll start there, with this odd-sounding little story:

> A squirrel and a cat and a dog played a game. They played the game a lot. The cat chased the squirrel, and the dog chased the cat. The friends played the game yesterday. The friends are a dog and a cat and a squirrel.

The Markov Chain is made up of nodes, one node for each word in the text. We're going to use this to build sentences, so I'll additionally add some special nodes, "BoS" and "EoS" to mark the beginnings and endings of sentences.

> `BoS` A squirrel and a cat and a dog played a game `EoS`. `BoS` They played the game a lot `EoS`. `BoS` The cat chased the squirrel, and the dog chased the cat `EoS`. `BoS` The friends played the game yesterday `EoS`. `BoS` The friends are a dog and a cat and a squirrel. `EoS`

To create the Markov Chain, move word-by-word through the sentence. At each word, make a note of the word that follows it. If you encounter the same word more times, keep recording each next word. For instance, the word `the` is followed the first time by `game`, so start a record for `the`, then document the occurrence of `game` you see following it.

```
the: {game: 1}
```

The second time you see `the`, it is followed by `cat`. Add that to the record.

```
the: {game: 1, cat: 1}
```

The next `the` is followed by `squirrel`, the next by `dog`, and the next by another `cat`. Keep adding to the record.

```
the: {game: 1, cat: 2, squirrel: 1, dog: 1}
```

Do that for every word, and you end up with this:

```
BoS: {a: 1, they: 1, the: 3}
a: {squirrel: 2, cat: 2, dog: 2, game: 1, lot: 1}
squirrel: {and: 2, EoS: 1}
and: {a: 4, the: 1}
cat: {and: 2, chased: 1, EoS: 1}
dog: {played: 1, chased: 1, and: 1}
played: {a: 1, the: 2}
game: {EoS: 1, a: 1, yesterday: 1}
the: {played: 1}
the: {game: 2, cat: 2, squirrel: 1, dog: 1, friends: 2}
lot: {EoS: 1}
chased: {the: 2}
friends: {played: 1, are: 1}
yesterday: {EoS: 1}
are: {a: 1}
```

This is your trained Markov Chain, graphically it looks like this:

{: .blog-figure-75 }
{% include image.html url="/assets/img/blog/markov-chain/chain_1.png" description="markov chain 1" %}

Here, thicker arrows represent more frequent transitions. For instance, `the` is followed by `game` twice, so the arrow from `the` to `game` is thicker than the arrow from `the` to `dog`. To querry the your AI, start at the `BoS` and make a weighted random move (thicker arrows have a better chance) to the next word. Continue this process until you reach the `EoS`. Here are some examples of sentences you might make:

* The dog chased the game a game.
* A cat and the squirrel and a dog played the dog and a squirrel and the friends are a lot.
* The cat chased the friends are a squirrel.
* They played a cat and a squirrel and the dog played a lot.

Those sentences *almost* make sense. The AI is just picking words at random, but it's picking words that are likely to follow the words that came before them. This is the Markov Chain in action.

## How can we improve this?

What if, instead of looking back one word, we looked back two? The word `the` could be followed by almost anything, but `chased the` and `played the` are much better clues. Looking back *two* words, we end up with a chain like this:

{: .blog-figure-75 }
{% include image.html url="/assets/img/blog/markov-chain/chain_2.png" description="markov chain 2" %}

Here are some sentences from our more advanced Markov Chain:

* The friends played the game yesterday.
* They played the game a lot.
* The friends are a dog and a dog played a game.
* A squirrel and the dog chased the squirrel and a squirrel and the dog chased the cat chased the cat.

Some of these sentences are a little more coherent, but there's a problem. Two of these sentences are directly from the story. Why?

Did you notice in the first Markov Chain that a few of the nodes were circled in red? Did you notice that a lot more were circled in red in the second Markov Chain? These red nodes are positions from which there is only one place to go. For instance, if your Markov Chain starts a sentence with `The friends`, the next three words *will be* `played the game`. There is no other option. These nodes are not intelligent, they are deterministic. Our AI doesn't know enough about sentences that start with `The friends` to do anything "intelligent" with them.

Here is a Markov Chain, trained with the same data, that looks back *three* words:

{: .blog-figure-75 }
{% include image.html url="/assets/img/blog/markov-chain/chain_3.png" description="markov chain 3" %}

And here are some sentences it generates:

* The friends are a dog and a cat and a squirrel.
* The friends played the game a lot.
* The cat chased the squirrel and the dog chased the cat.
* They played the game yesterday.

Nice sentences, but most of them are directly from the story, because most of the nodes are deterministic. And it would have happened a lot sooner if I hadn't used such a strange, repetitive story.

## Will more data help?

Yes. These sentences were produced by a Markov Chain trained on the novel [*Moby Dick*](https://www.barnesandnoble.com/w/moby-dick-herman-melville/1116670757?ean=9780142437247) (it's not a thin book), looking one word back:

* Beware of classical engravings from him out the door to but the fishery.
* Morning the special leviathanic proportions the mechanical I fill to dart it and fought my butter-boxes cried Stubb then so that had assured indeed they all legs and said no means of the whole affair.
* Had just hovered for the waves were forced into these blessed saturday night which in a peaked.
* As for the humped herds are so important an old bottles and pointing his trowsers pockets.

Pretty non-sensical, but only around 5% of the words are deterministic, either because they only appear once, or because they are always followed by the same word.

And here's the same thing looking two words back:

* A good lifetime the census of men but also from the boat is still in force I proceed to set an example.
* As for you can't help it but as the insect does to the human fingers in the face of my doors.
* Nor is it for a good start when the former that he should soon become my shipmate though but a combing wave hurled themselves bodily inboard again the third in the porch.
* Upon this fleece holding his tongs in the far rush of the flood.

These make a bit more sense---maybe---but we're already 43% deterministic. That's 43% of two-word strings found, not 43% of *unique* two-word strings, which would be much higher (82%).

Some of these are fine. The word pair `a sort` appears 53 times, always followed by `of`. It's not a terrible thing to copy such patterns verbatim, but our AI is nevertheless becoming more deterministic, and not all word triplets are canonical. `glided by as`, `sea fell over`, `of pale forked` and around 90 thousand other phrases are have now been "hard coded" into our AI.


Here's the same thing looking three words back:

* In compliance with the standing order of his commander to report immediately and at any one of his own gums like a chimney hag.
* As i live he's comparing notes looking at his thigh bone thinks the sun is breaking through the clouds are rolling off serenest azure is at hand.
* If your banker breaks you snap if your apothecary by mistake sends you poison in your pills you die.
* Porpoise meat is good eating you know.

Good writing? It should be, the last two sentences are quoted directly from the book. At three-words back, our AI is 80% deterministic. At four-words back, 92%---at that point, you're basically just picking whole senteces out of the training text.

{: .ext-emphasis }
We've increased our data over FOUR HUNDRED THOUSAND PERCENT, but our strategy is still busted at three to four words back.

A big, thick book like Moby Dick looks like a lot of data, but it's not.

## So how many books is enough?

You could make a nice start with ALL of the books. Not just all of the [Melville](https://en.wikipedia.org/wiki/Herman_Melville)[^1] books, all of the books. But even that would only get you so far. Once you'd exhausted all the available training data, you'd have to build a bit more by looking at synonyms of words. With a sophisticated program, you could use sentences about labradores, beagles, and terriers to teach your AI more about dogs. You could translate sentences about *perros*, *hunde*, or *cani*.

The Markov Chain is just one criterion you can use to select a next word. You can do more with the same amount of data if you leverage other criteria, but all such criteria will face the same data limitations. Your AI is **HUNGRY**, and no amount of processing power will ever change that. 

[^1]: [Herman Melville](https://en.wikipedia.org/wiki/Herman_Melville) was a prolific American author in the 19th century. He wrote [Moby Dick](https://www.barnesandnoble.com/w/moby-dick-herman-melville/1116670757?ean=9780142437247) (1951) along with several other novels, short stories, and volumes of poetry.
