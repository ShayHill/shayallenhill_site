---
layout: post
title: "Deploy Your First Baby Bot on Heroku"
date: 2022-05-23 14:10:41 -0500
tags:
categories: [programming]
author: Shay Hill
excerpt: So, you’re a programmer (or not) who has built (or downloaded) their first bot. What's now?
post_image: "/assets/img/blog/deploy-your-first-baby-bot-on-heroku/small-4021843_1920.jpg"
---

# Your First Baby Bot

So, you’re a programmer (or not) who has built (or downloaded) their first bot. A bot can be a lot of things, but this article is focused on scripts that interface with an [Application Programming Interface (API)](https://en.wikipedia.org/wiki/API) to read or write information from or to a web-based application like Twitter, Todoist, etc.

Specifically, this article is for [Todoist](https://todoist.com/app/today) users who want to run one of the many available bots (especially Python bots) that enhance Todoist functionality. However, this will be useful for anyone who has managed to get a social-media bot, data-sync, app-automation, or similar working on their laptop and now wants to run it on the cloud. If you’re a Todoist user who hasn’t even gotten that far, read through. If you have gotten that far, skip down to “deploy your bot”.

<blockquote class="big-blockquote" markdown="1">

## Todoist users: Got 5 minutes? Let’s catch you up

* Todoist is a popular task-management app.
* Todoist has an [Application Programming Interface (API)](https://github.com/Doist/todoist-api-python) that allows programmers to read and write information stored inside the Todoist application.
* You can take advantage of this, even if you aren’t a programmer, because helpful people have written scripts to add or tweak Todoist functionality

For example, you can download [this script](https://github.com/ShayHill/todoist_bot) and call it with

~~~ powershell
python main.py -a <YOUR-API-TOKEN> --serial "next_action -n"
~~~

... to make Todoist tag the next step in any marked ("Project -n") project. That will clear a lot of noise from your task list, and if you have just a little bit of background, you can get it running in 5 minutes.

A lot of people have gotten this far. If you haven’t:

* download and install [Python](https://www.python.org/)
* download and install [Git](https://git-scm.com/)
* copy YOUR-API-TOKEN from the [Todoist website](https://todoist.com) (click profile then integrations then developer)
* now open a prompt and type (replacing `<YOUR-API-TOKEN>` with your api token from todoist.com) …

~~~ powershell
git clone https://github.com/ShayHill/todoist_bot
cd todoist_bot

pipenv shell
pipenv install -r requirements.txt
python main.py -a <YOUR-API-TOKEN> --serial "next_action -n"
~~~

If you’ve never installed Python, and never worked with Git, you’ve got some homework to do—or maybe a friend to call. If you have, then all of that might have taken you five minutes. Your bot is alive! Now test it out.

Open Todoist and add the suffix "-n" to one of your projects, sections, or tasks (e.g., "my project -n"). In a few seconds, the next available (sub)task underneath it will be labeled "next_action". Better than that, even though the script is running on your computer, Todoist will function this way on *any* computer and on your phone.

… that’s as long as the script is running. If you shut the script window, turn off your computer, lose your WiFi, whatever, Todoist will no longer automatically tag tasks.

### Got another 5 minutes?

The idea is to take whatever script is running on your computer and run it on a web server. This is a common thing to do, but the documentation is overwhelming and mostly assumes you want to host a website. I’m going to leave out the noise and tell you *exactly* what to do.

</blockquote>

## Deploy your Bot

No explanations, no guarantees, and some bad practice, but sometimes you just need to see ONE WORKING EXAMPLE. Here it is. Get this working then grow from there.

* download, install, and sign up for an account at [Heroku](https://id.heroku.com/login). You will have to give Heroku a credit card number, and Heroku will bill you based on usage. Expect to pay about $5 a month to run bot like this.

* open a prompt and type …

~~~ powershell
git clone https://github.com/Hoffelhas/autodoist
cd autodoist
heroku login
~~~

* open and edit (or create) the file called `Procfile` (no file extension)
* add or remove arguments to create the functionality you desire
* replace YOUR-API-TOKEN with your api token from [Todoist](https://todoist.com/app/today)

~~~ raw
worker: python main.py -a <YOUR-API-TOKEN> --serial "next_action -n" "blocking -b" --parallel "actionable -a" --all "parked -p" "focus -f"
~~~

… or `worker: python autodoist.py -a <YOUR-API-TOKEN> -r` or `worker: python my_twitter_bot.py` or `worker: python my_other_kind_of_bot.py` or whatever. Just don’t leave any blank lines, comments, or trailing spaces. Heroku is picky.

* go back to your prompt and type …

~~~ powershell
heroku local
~~~

Heroku local should run the script from your computer so you can make sure everything is working.

*To keep this simple, I’m now going to ask you to “commit your api token” which is less-than-perfect practice. Conceivably, someone could access this token and then your tasks. If you’re worried about it, get your bot working then go back to todoist.com > profile > integrations > developer and request a new token. This will of course break your bot, but you’ll know most of what you need to bring it back to life. The long-term solution is Heroku “config vars”, but that is a lesson for another day.*

* in a command prompt …

~~~ powershell
heroku create
git add .
git commit -m "my bot is alive"
git push heroku master
heroku ps:scale worker=1
heroku logs --tail
~~~

If everything went well. You’re now seeing your bot at work. Just sit back and wait for task automation, data synchronization, or social-media superstardom.
