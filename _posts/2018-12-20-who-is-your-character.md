---
layout: post
title: "(Maybe) Everything You'll Ever Need to Know About Python Imports and Project Structure"
date: 2023-01-14 14:14:54 
tags: 
categories: [programming]
author: Shay Hill
excerpt: It isn't that hard, but it is a well-kept secret.
post_image: "/assets/img/blog/python-project-structure/shipping-gcfa65e84f_1920.jpg"
---


<style>

.tree img {
    margin-left:10px;
    margin-right:auto
}

</style>



# Got a few hours?

Follow [this link](https://docs.python.org/3/reference/import.html) for the Python import system in seven-thousand words. If that's not enough, [Stack Overflow](https://stackoverflow.com) may have another ten thousand words. Still not sure? Don't worry, topics like this keep sites like [Ask Python](https://www.askpython.com/), [Geeks For Geeks](https://www.geeksforgeeks.org/), and [Discuss.Python](https://discuss.python.org/) in business.

Read these, and you will learn about "running as a module vs. running as a script", "editable installs", "the pros and cons of altering sys.path", "Pytest's unusual import conventions", "\_\_init\_\_.py whack a mole", and a new word, "antipattern" that you can use in your own online conversations.

You might even learn a painless way to handle Python imports, but probably not. It isn't that hard, but it is a well-kept secret. And for good reason. I've had a draft of this article in my head for months, but it wasn't until I started using [Poetry](https://python-poetry.org/) that I found a method I could explain in a two-minute read.

# Starting with the basics

## import from the standard library

You can reach the standard library from anywhere with

~~~ python
from string import ascii_uppercase
~~~

## import from an installed package

After `pip-install`-ing a package into a Python install or environment, you can import it as you would a package in the standard library.

~~~ python
from numpy import ndarray
~~~

## import local code

{% include ext-emphasis.html content="This works." %}

{: .tree }
{% include image.html url="/assets/img/blog/python-project-structure/flat.png" alt="" description="" %}

You can import from any module to any module with

~~~ python
from module_1 import some_function
from module_2 import some_function
~~~

And you can run any module with

~~~ powershell
> python module.py
~~~

{% include ext-emphasis.html content="This also works, with some important caveats." %}

{: .tree }
{% include image.html url="/assets/img/blog/python-project-structure/simple_dirs_tree.png" alt="" description="" %}

You can import any module in a subfolder, starting with the subfolder name. This is required even when importing into the same subfolder.

~~~ python
# import subfolder_1.module_1b from main.py
from subfolder_1.module_1b import some_function

# import subfolder_1.module_1b from subfolder_1/module_1a.py
from subfolder_1.module_1b import some_function
~~~

Start with a (red) subfolder name, no matter where you're importing to. This means you **cannot** import `main.py` from a module in a subfolder, because Python will not know about the folder (here named "folder") above it.

You can run any module in the top folder with

~~~ powershell
> python main.py
~~~

But you will have to run modules in subfolders with

~~~ powershell
> python -m subfolder_1.module_1b
~~~

# Here's where it all goes wrong

If you follow a few simple rules, you can lay out your code so modules are available where you need them. If you run your code the "right" way from the "right" place, everything will work. That will be fine till some other person, or some other tool, needs to run your code. Users should be able to figure it out, but tests and linters and build systems and PyPi won't.

At that point, you need a whole *other* language in `setup.py` or `pyproject.toml` to tell these tools how you've set everything up. And that's why the answer to "Why doesn't x linter recognize my imports?" or "How do I import from y?" doesn't fit neatly into a StackOverflow reply. The situation is so bad that people do the wrong thing for **years**, and even experienced Python coders give wrong answers to these questions.

Again, there are far too many ways to do this, but here's one that will work almost every time.

> **I can't stand an answer that starts with installing yet another tool**, especially when the tools I've already installed aren't working the way I expect them to. But here we are. You can't fix this by updating your Python code, because there's probably nothing wrong with your Python code *or* with your project structure. What you're most likely missing is *outside* all of that. So...

We are going to install and run a tool called [Poetry](https://python-poetry.org/). If you like it, keep using it. If not, you can watch what it does and learn a lot about what Python expects from a project.

~~~ powershell
pip install poetry
poetry new --name project_name --src folder_name
poetry install
~~~

With these commands, [Poetry](https://python-poetry.org/) will create the following files and folders

{: .tree }
{% include image.html url="/assets/img/blog/python-project-structure/poetry_default_tree.png" alt="" description="" %}

... including the `pyroject.toml` file you will need for the next step: installation into your virtual environment. Poetry will "install" your code in a virtual environment the same way you might install `numpy` or `PIL` or `requests`, so you will be able to reach *any* module in your `src/project_name` folder the same way you reach any other installed module.

Here is the same structure with a few more files so we can see some examples.

{: .tree }
{% include image.html url="/assets/img/blog/python-project-structure/with_added_files_tree.png" alt="" description="" %}

You can import modules in `project_name` from anywhere in your project the same way you can import from the standard library or from a pip-installed module.

~~~ python
# in main.py
from project_name.main import some_function
from project_name.subdirectory.in_subdir import some_function

# in tests.test_in_subdir
from project_name.main import some_function
from project_name.subdirectory.in_subdir import some_function

# in any other Python file in folder_name
from project_name.main import some_function
from project_name.subdirectory.in_subdir import some_function
~~~

If you open the empty `project_name/__init__.py` and add

~~~ python
from project_name.main import some_function
from project_name.subdirectory.in_subdir import some_other_function

__all__ = ["some_function", "some_other_function"]
~~~

... you can shorten those imports to

~~~ python
from project_name import some_function, some_other_function
~~~

> In any case, leave the `__init__.py` files in place. Python won't *always* need them, but some of the linters will.

You will never use `src` when importing. Start at the red folder name. The `src` folder is there to **intentionally** break some of the other import mechanisms so you don't rely on them now only to be frustrated later.

So, there it is, (maybe) everything you'll ever need to know. I didn't write it as short as I could, but it's still short. I hope I've saved you a lot of time and at least a few tears.




