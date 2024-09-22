---
layout: post
title: "Install and Configure Vim in Windows"
date: 2024-09-21 17:13:21 -0600
tags:
categories: [programming]
author: Shay Hill
excerpt: Install Vim in Windows and configure it for a nice experience.
post_image: "/assets/img/blog/vim-in-windows/chemistry_set.png"
---

<style>
%% blockquote.bq_neutral {
%%     border-left: 4px solid #aaaaaa;
%% }
%% blockquote.bq_opportunity {
%%     border-left: 4px solid #ffc000;
%% }
%% blockquote.bq_improved {
%%     border-left: 4px solid #0070c0;
%% }
</style>

# Install Vim

This one is easy, because we're not going to compile Vim, but there are some tricks if you aren't familiar with Windows.

Go the [the Vim.org download page](https://www.vim.org/download.php), download the exe file for your architecture (32 or 64 bit), run it, and accept all the defaults. This will add a few icons to your desktop that you probably don't want, but it's easy to delete them later.

The installer will add Vim to your Path environment variable, but it may *not* update an existing Vim path. So, if you have `C:\Program Files\Vim\vim90` in your path, the installer may not update that to `C:\Program Files\Vim\vim91` (or whatever the current version is as you are reading this).

## Editing the Path Environment Variable

If you are completely unfamiliar with Windows, let's quickly go through this. You don't *have to* have Vim in your path, you could just use shell aliases, but Windows has a nice 'open in Vim' context-menu option that makes it nice to have gVim in your path.

* Press the Windows key
* Search for "Environment Variables" and click the "Best Match"
* This will bring up the System Properties dialog, which has a link, Environment Variables, near the lower-right corner. Click there.
* The "User variables for username" are in the top half of the Environment Variables dialog. For now, you're interested in the Path variable
* Double click the Path variable, and make sure you see the path to your current Vim installation.
* If not, click "Edit" then "Browse" then navigate to `C:\Program Files\Vim\vim91` (or whatever the current version is) to add it.

### Some Nuance with Environment Variables

* Environment variables are read when applications are opened, so changes to environment variables will not take effect until you open a new window.
* You have to back out (click "OK") *twice*, going all the way back to the System Properties dialog, before the variable is actually changed. This one has gotten me many times.

## Create a Vimrc

If you open gVim now, you will have a fairly nice experience. Filetype detection and syntax highlighting will work, backspace will behave as you expect it to, and commands will autocomplete.

However, once you create your own configuration in

```
~\vimfiles\vimrc
```

Vim gets (arguably) worse! This because is is because Bram and others configured some nice default behaviors in

```
C:\Program Files\Vim\vim91\defaults.vim
```

But these defaults aren't, strictly speaking, defaults, because this is not how Vim will look and behave with *no* configuration. When you create your own `vimrc` file, Vim reads your `vimrc` *instead of* `defaults.vim`, so you get true "out of the box" Vim behavior: no filetype detection, no syntax highlighting, and 1970s-style backspace behavior.

This is all we'll configure for now. Open gVim (not Vim itself. Wait until we have a better shell to run it in) from the Windows menu. Run this command:

```
:e ~\vimfiles\vimrc
```

and create a simple vimrc with this content:

```vim
vim9script

## nice defaults from Bram and the The Vim Project
source $VIMRUNTIME/defaults.vim 
```

This will preserve the nice defaults. The `vim9script` is optional, but the rest of this guide will assume you have it set.

# Install Cross-Platform PowerShell


There are two versions of PowerShell: Windows PowerShell (blue icon) and cross-platform PowerShell (black icon). Windows comes pre-installed with blue-icon PowerShell, but if you open it, you will see a prompt to install cross-platform (black-icon) PowerShell. Ctrl-click the link in this prompt and [install the latest version of "PowerShell 7"](https://learn.microsoft.com/en-us/powershell/scripting/whats-new/migrating-from-windows-powershell-51-to-powershell-7?view=powershell-7.4) (cross-platform, black-icon PowerShell). Accept all defaults during install.

Once installed, PowerShell 7 will be the default when you run Windows Terminal. You can run Windows Terminal by searching for it in the start menu or by holding the `windows key`, pressing `x`, then releasing both keys and pressing `i`. When I use the name "PowerShell" from here on, I am referring to cross-platform, black-icon, PowerShell 7.

## Configuration

If you don't already have a PowerShell config, create one by running

```powershell
new-item $profile -itemtype file
```

from PowerShell. This will create a PowerShell profile at

```
~\Documents\PowerShell\Microsoft.PowerShell_profile.ps1
```

We will add aliases to this as we go. For now, here is the format for those aliases:

```powershell
Set-Alias -Name black -Value 'C:\Users\shaya\AppData\Local\Programs\Python\Python312\Scripts\black'
Set-Alias -Name isort -Value 'C:\Users\shaya\AppData\Local\Programs\Python\Python312\Scripts\isort'
```

### Open a New PowerShell Tab in the Same Directory

When you open a new tab in PowerShell, that tab will be open to a system folder or your home directory, depending on how you have it configured. If you're working on a project in Vim, and you want to open a tab to run git or pre-commit or something else, then you probably want to open a new tab in the project directory.

[This page](https://learn.microsoft.com/en-us/windows/terminal/tutorials/new-tab-same-directory) explains how to configure PowerShell to open a new tab in the same directory as the current tab. It explains a few-dozen other approaches as well, so I'll put the relevant information here.

Copy this code into your PowerShell profile:

```powershell
function prompt {
  $loc = $executionContext.SessionState.Path.CurrentLocation;

  $out = ""
  if ($loc.Provider.Name -eq "FileSystem") {
    $out += "$([char]27)]9;9;`"$($loc.ProviderPath)`"$([char]27)\"
  }
  $out += "PS $loc$('>' * ($nestedPromptLevel + 1)) ";
  return $out
}
```

Now, close and reopen PowerShell, then press `Ctrl+Shift+D` (D for Duplicate) in PowerShell to to open a new tab in the same directory as the current tab.
### Tell Vim About PowerShell

Start PowerShell (`winkey-x` then `i`), open Vim inside PowerShell, then add this to `~vimfiles\vimrc`.

```vim
if has("windows")
    set shell=pwsh
endif
```

To let Vim know to open terminals in cross-platform PowerShell. The options `shell=pwsh` and `shell=powershell` are not the same. The latter is for Windows (blue-icon) PowerShell, which isn't a nice experience.


# Install Python

Don't do it *yet*, but you're going to go to [Python.org](https://www.python.org/downloads/) and install every version of Python you intend to support with your projects.

But, again, don't do that yet, particularly if you've already installed some plugins with Vim.

First, start with a relatively new and stable version of Python. No prereleases and no new releases. Vim doesn't ship with it's own version of Python. It will try to use the newest version of Python you have. We'll first have to tell Vim *which* version of Python we want to use.

Open your `~vimfiles\vimrc` file and add the following (if your "relatively new and stable" version of Python is 3.11):

```vim
if has("windows")
    var local_programs = expand('$HOME/AppData/Local/Programs')
    execute 'set pythonthreehome=' .. local_programs .. "/Python/Python311"
    execute 'set pythonthreedll=' .. local_programs .. "/Python/Python311/python311.dll"
endif
```

There are a few different formats Vim will accept for Windows links. This `execute` version is the one I prefer, because we're going to keep adding links to our `local_programs` folder.

You may find that Vim and all your plugins will work just fine without setting `pythonthreehome` and `pythonthreedll`. Vim is pretty smart about finding your Python install. However, that could break at any time if you install a version of Python Vim or one of your plugins doesn't support.

**OK, now** install the other versions of Python you intend to support. To follow along with this guide, accept all defaults when installing.

### Older Python Versions

Having the exact Python versions you intend to support installed on your machine is less important than it used to be, because we can test whatever versions we like with continuous integration. So, when it comes to older versions of Python, you don't *have* to compile the latest security release.

If you find a source only release of  an older Python, you can scroll down to find the note

> **No installers**
> According to the release calendar specified in [PEP 569](https://www.python.org/dev/peps/pep-0569/), Python 3.8 is now in the "security fixes only" stage of its life cycle: 3.8 branch only accepts security fixes and releases of those are made irregularly in source-only form until October 2024. Python 3.8 isn't receiving regular bug fixes anymore, and binary installers are no longer provided for it. **Python 3.8.10** was the last full _bugfix release_ of Python 3.8 with binary installers.

... which will direct you to the latest binary. Or you can just not install it at all and rely on ci for your tests. The latter version will be safer, but my brother still works at a company running Python 2.7 in 2024.

### The Python Launcher

Windows does not add `python` to your path. Instead it adds [the Python launcher](https://docs.python.org/3/using/windows.html#launcher), `py`. If you want to run `python` from PowerShell, run `py` to run the latest version. Run `py -3.12` to run another version. To run another version by default, create a new User Environment Variable, `PY_PYTHON` and set the value to the default you'd like to run. For example, `3.12`.

I like this setup, because `python` will *only* work from inside a virtual environment. So, any script you set up to run `python` will only work from a virtual environment.


# Install Git

Go to [git-scm.com](https://git-scm.com/download/win) and click `64-bit Git for Windows Setup.` (or 32-bit if you're on a 32-bit system). Run the installer.

This is the only time in this guide I will suggest you change a default. Keep every default except one:

"Adjusting the name of the initial branch in new repositories" has it's own page in the install dialog. The choices are

*  Let Git decide (the default)
*  Override the default branch name for new repositories

As of this writing, Git and GitHub are using different default branch names, which can get annoying. A lot of online help uses Git's `master`, but the scripts on GitHub use `main`. I suggest you change the default branch name (select the Override option) to `main` to match GitHub to save the headaches.

### Configure Git from PowerShell

Open PowerShell and run the following commands:
```powershell
git config --global user.email "your@email.com"
git config --global user.name "Your Name"
git config --global core.editor "'C:\Program Files\Vim\vim91\vim.exe' -f -i NONE"
git config --global merge.tool vimdiff
git config --global diff.tool vimdiff
git config --global core.excludesFile "$Env:USERPROFILE\.gitignore"
```

You already selected Vim during install, but maybe a Git internal Vim. Whatever Vim it is, it doesn't source your vimrc. You'll want to set up Vim here.

Don't let the `--global` flag misinform you. These are settings for one user. These commands update a file in your home directory called `.gitconfig`. You can edit this file later or re-run the commands if you don't like what I've put here, but these are the standard settings for Vim users. If you prefer, you can use `gvimdiff` instead of `vimdiff` for git tools. In fact, gvim is a little quicker on Windows than Git through PowerShell. But usually you're working in Git through the terminal, and your heaviest "tool" usage will be opening up a quick instance for commit messages.

### Other Things That Come With Git

The installer will add `git` to your "System environment" Path (not your "User variables" Path).

The Git installer also provides Curl and Bash. Curl will be on your path for plugins like vim-instant-markdown. You can add bash to your path or just create an alias in your PowerShell profile. It's not necessary for Vim, but it's convenient and already installed if you know Bash. Add this to your PowerShell profile.

```powershell
Set-Alias -Name bash -Value 'C:\Program Files\Git\bin\bash.exe'
```


# Install Ripgrep

"Grepping" is a big part of navigating through projects. In Windows, Vim will try to use a grep alternative. I don't remember the name. It works in cmd, but it freezes PowerShell, so we don't want it. Ripgrep is a nice alternative.

*  Go to [github.com/BurntSushi/ripgrep/releases](https://github.com/BurntSushi/ripgrep/releases)
*  Click the version number with (Latest) printed beside it.
*  Scroll down to "Assets".
*  Download the `msvc.zip` file for your architecture (64 or 32 bit). Example: `ripgrep-14.1.1-i686-pc-windows-msvc.zip`
*  Extract the zipfile somewhere. Windows doesn't have a dedicated `bin` folder. Some extract executables to

```
C:\Windows\Program Files\
```

I prefer to extract them to

```
~\AppData\Local\Programs\
```

That is the folder I will link to in the next step.

### Tell Vim to use Ripgrep

Add the following to your `~\vimfiles\vimrc` file. This will tell Vim to use Ripgrep when you use the `:grep` command.

```vim
if has("windows")
    var local_programs = expand('$HOME/AppData/Local/Programs')
    var rg = local_programs ..  '/ripgrep-13.0.0-x86_64-pc-windows-msvc/rg.exe'
    if executable(rg)
        set grepprg = rg\ --vimgrep\ --no-heading
    else
        echoerr "rg not found. Install ripgrep to use :grep"
    endif
endif
```

Once you get everything set up, consider the [ctrl-sf](https://github.com/dyng/ctrlsf.vim) plugin, which will make use of your newly installed and nicely linked ripgrep.


# Install Lua

This step is optional. Lua is required for a few Vim plugins, which you may or may not want to use. I use it for `vim-instant-markdown`.

*  Go to [https://luabinaries.sourceforge.net/download.html](https://luabinaries.sourceforge.net/download.html)
*  Download [lua-5.4.2_win64_dllw6_lib.zip](https://sourceforge.net/projects/luabinaries/files/5.4.2/windows%20libraries/dynamic/lua-5.4.2_win64_dllw6_lib.zip/download\|lua-5.4.2_win64_dllw6_lib.zip).
*  You will find another file there, `lua-5.4.2_Win64_bin.zip`. You do not need that file.

Extract [lua-5.4.2_win64_dllw6_lib.zip](https://sourceforge.net/projects/luabinaries/files/5.4.2/windows%20libraries/dynamic/lua-5.4.2_win64_dllw6_lib.zip/download\|lua-5.4.2_win64_dllw6_lib.zip) somewhere. I use

```
~\AppData\Local\Programs\
```

### Tell Vim Where to find Lua

Edit `~\vimfiles\vimrc` and add the following:

```vim
if has("windows")
    var local_programs = expand('$HOME/AppData/Local/Programs')
    execute 'set luadll=' .. local_programs .. '/lua-5.4.2_Win64_dll17_lib/lua54.dll'
endif
```

# Gvim Fullscreen

This step is optional, but if you dislike the toolbar's intruding into your immersive coding experience, you might not feel that way. This executable will allow you to fullscreen gVim.

*  Compile from source: [https://github.com/movsb/gvim_fullscreen](https://github.com/movsb/gvim_fullscreen) ... download [https://github.com/movsb/gvim_fullscreen/releases](https://github.com/movsb/gvim_fullscreen/releases).
*  Copy gvimfullscreen.dll to `~/vimfiles/`.

### Tell Vim Where to Find the DLL

Add the following line to your vimrc.

```vim
var gvim_fullscreen = expand('$HOME/vimfiles/gvim_fullscreen.dll')
noremap <C-F11> <esc>:call libcallnr(gvim_fullscreen, 'ToggleFullscreen', 0)<cr>
noremap <C-F12> <esc>:call libcallnr(gvim_fullscreen, 'ToggleTransparency', '255,180')<cr>
```

Now you can fullscreen gVim with `Ctrl+F11` and toggle transparency with `Ctrl+F12`. I always thought transparency was kind of tasteless, but I've found it nice for re-typing text from a PDF or other source.

For what it's worth, PowerShell will fullscreen Vim when you press `F11` at the cost of stealing this mapping from [vimspector](https://github.com/puremourning/vimspector).


# Install Visual Studio Build Tools

This step is optional. It's a fairly big install, but you will need this for some Python libraries like [llama_index](https://github.com/run-llama/llama_index). If you're into things like that, you're going to need it at some point. Here's the quick way to get the important parts up and running.

*  Got to [visualstudio.microsoft.com/visual-cpp-build-tools/](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
*  click `Download Build Tools`
*  run the installer
*  select the C++ compiler when running the installer
*  Install "Desktop development with C++"
*  You could *probably* go into "Individual Components" and install "C++ CMake tools for Windows" and "Windows 11 SDK" only, but the entire "Workload" is only 1.75GB and it's not worth the hassle to figure out what you need and what you don't.


# Install Lazygit

This step is optional, but [Lazygit](https://github.com/jesseduffield/lazygit/) is fun and cool and useful. Like all Git interfaces, it's got [issues](https://github.com/jesseduffield/lazygit/issues)—as I write this, 666 open issues—but in addition to being fun and cool, it's a chance to try out a new Windows tool: `winget`. And don't let the open issues put you off. As I said (and if you'll excuse a little fun with the coincidence), it's *the nature of the beast*. Which may be a big part of the reason you're installing Vim in the first place (fewer interfaces).

Run `winget install -e --id=JesseDuffield.lazygit`, and winget will install Lazygit for you. Close and restart your Windows Terminal, navigate to a Git project, and type `lazygit` to have a look.
