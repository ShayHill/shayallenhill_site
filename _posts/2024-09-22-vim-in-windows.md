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

code {
    background-color: #666666;
    color: #f8f8f2;
    border-radius: 0.3em;
    padding: 4px 5px 6px;
    %% white-space: nowrap;
}
</style>

# Install Vim

This is an obvious first step, and it's an easy one, because we're not going to compile Vim. But there are some tricks if you aren't familiar with Windows.

Go to [Releases · vim/vim-win32-installer (github.com)](https://github.com/vim/vim-win32-installer/releases), download the exe file for your architecture (32 or 64 bit), run it, and accept all the defaults. This will add a few icons to your desktop that you probably don't want, but it's easy to delete them later. Elsewhere in this guide, we're going to use `winget`, but Vim itself suggests downloading and installing from GitHub.

The installer will not add `vim` and `gvim` to your Path environment variable. You can alias them in PowerShell as shown in the **Install Cross-Platform PowerShell** section below or add them to your Path.

## Editing the Path Environment Variable

If you are completely unfamiliar with Windows, let's quickly go through this. You don't *have to* have Vim in your path, you could just use shell aliases, but if you want to, there are multiple ways to do it. I'll describe two. I prefer Option Two, because there's less room for error, and you'll probably end up there eventually to clean up mistakes made with Option One. Option One is for people who wish to script their entire device configuration.

### Option One, Command Line

Open PowerShell and enter (If you've installed Vim91)

```powershell
[Environment]::SetEnvironmentVariable("PATH", "$($env:PATH);C:\Program Files\Vim\vim91", [EnvironmentVariableTarget]::User)
```

### Option Two, GUI

* Press the Windows key
* Search for "Environment Variables" and click the "Best Match"
* This will bring up the System Properties dialog, which has a link, Environment Variables, near the lower-right corner. Click there.
* The "User variables for username" are in the top half of the Environment Variables dialog. For now, you're interested in the Path variable
* Double click the Path variable, and make sure you see the path to your current Vim installation.
* If not, click "Edit" then "Browse" then navigate to `C:\Program Files\Vim\vim91` (or whatever the current version is) to add it.

### Some Nuance with Environment Variables

* Environment variables are read when applications are opened, so changes to environment variables will not take effect until you open a new window. There are other ways, but that's the easy way.
* You have to back out (click "OK") *twice*, going all the way back to the System Properties dialog, before the variable is actually changed. This one has gotten me many times.

## Create a Vimrc

If you open gVim now, you will have a fairly nice experience. Filetype detection and syntax highlighting will work, backspace will behave as you expect it to, and commands will autocomplete.

However, once you create your own configuration in

```
~\vimfiles\vimrc
```

Vim gets (arguably) worse! This is because Bram and others configured some nice default behaviors in

```
C:\Program Files\Vim\vim91\defaults.vim
```

But these defaults aren't, strictly speaking, defaults, because this is not how Vim will look and behave with *no* configuration. When you create your own `vimrc` file, Vim reads *your* `vimrc` *instead of* `defaults.vim`, so you get true "out of the box" Vim behavior: no filetype detection, no syntax highlighting, and 1970s-style backspace behavior.

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

There are two versions of PowerShell: Windows PowerShell (blue icon) and cross-platform PowerShell (black icon). Windows comes with blue-icon PowerShell pre-installed, but if you open it, you will see a prompt to install cross-platform (black-icon) PowerShell.

Either ctrl-click the link in this prompt to [install the latest version of "PowerShell 7"](https://learn.microsoft.com/en-us/powershell/scripting/whats-new/migrating-from-windows-powershell-51-to-powershell-7?view=powershell-7.4) or run this command in blue-icon PowerShell

```powershell
winget install Microsoft.Powershell --source winget
```

If you install by downloading and running the executable, accept all the defaults.

Once installed, PowerShell 7 will be the default when you run Windows Terminal. You can run Windows Terminal by searching for it in the start menu or by holding the `windows key`, pressing `x`, then releasing both keys and pressing `i`. When I use the name "PowerShell" from here on, I am referring to cross-platform, black-icon, PowerShell 7.

If PowerShell 7 is not the default, or if you don't see black-icon PowerShell as a choice when adding a tab with the Windows Terminal down arrow in the tab bar, it's safe to go to

```
C:\Users\username\AppData\Local\Packages\Microsoft.WindowsTerminal_8wekyb3d8bbwe\LocalState
```

and delete `settings.json` and `state.json`. They will almost instantly regenerate, leaving your Windows Terminal in a default configuration (which should include PowerShell 7). Of course, you'll lose any configuration you've done, but it was probably broken anyway. Make a backup if you're worried about it.

## Configuration

If you don't already have a PowerShell config, create one by running

```powershell
new-item $profile -itemtype file
```

from PowerShell. This will create a PowerShell profile at

```
~\Documents\PowerShell\Microsoft.PowerShell_profile.ps1
```

You may wish to add aliases as we go. For now, here is the format for those aliases:

```powershell
Set-Alias -Name black -Value 'C:\Users\USERNAME\AppData\Local\Programs\Python\Python312\Scripts\black'
Set-Alias -Name isort -Value 'C:\Users\USERNAME\AppData\Local\Programs\Python\Python312\Scripts\isort'
```

### Open a New PowerShell Tab in the Same Directory

When you open a new tab in PowerShell, that tab will be open to a system folder or your home directory, depending on how you have it configured. If you're working on a project in Vim, and you want to open a tab to run git or pre-commit or something else, then you probably want to open a new tab in the project directory.

[This page](https://learn.microsoft.com/en-us/windows/terminal/tutorials/new-tab-same-directory) explains how to configure PowerShell to open a new tab in the same directory as the current tab. It explains a few-dozen other approaches as well, so I'll excerpt the relevant information here.

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

You can use winget or [Download Python \| Python.org](https://www.python.org/downloads/) executable files to install every version of Python you want to support. These are the supported versions of Python as I write this.

```powershell
winget install Python.Launcher --source winget
winget install Python.Python.3.8 --source winget
winget install Python.Python.3.9 --source winget
winget install Python.Python.3.10 --source winget
winget install Python.Python.3.11 --source winget
winget install Python.Python.3.12 --source winget
```

If you're installing using winget, also install the Python Launcher. If you're installing through the Python website, the executables will install the Python Launcher for you.

You may also want to install older versions, release candidates, or something else potentially not supported by Vim and it's plugins. **Don't do that yet!**

First, select a relatively new and stable version of Python---no prereleases and no "month-of" releases. Vim doesn't ship with it's own version of Python. Vim and it's plugins will try to use the newest version of Python you have. To avoid any problems, we'll tell Vim *which* version of Python we want to use. Open your `~vimfiles\vimrc` file and add the following (if your "relatively new and stable" version of Python is 3.11):

```vim
if has("windows")
    var local_programs = expand('$HOME/AppData/Local/Programs')
    execute 'set pythonthreehome=' .. local_programs .. "/Python/Python311"
    execute 'set pythonthreedll=' .. local_programs .. "/Python/Python311/python311.dll"
endif
```

From Vim, run the command `:py3 print("test")` to make sure you have it set up correctly.

You may find that Vim and all your plugins "just work" without setting `pythonthreehome` and `pythonthreedll`. Vim knows where to look for a typical Python install. However, that could break at any time if you install a version of Python that Vim or one of your plugins does not support.

As I write this, Python 13 is in prerelease, and Vim itself is not compatible. So not even `vim -u NONE` will get you past the errors. Go ahead and explicitly set these values in your vimrc.

---

**OK, NOW** install whatever exotic, specific, or decrepit versions of Python you'd like to have.

### The Python Launcher

If you install Python using winget, you will have a lot of new entries in your User Path environment variable.

```
C:\Users\shaya\AppData\Local\Programs\Python\Python312\Scripts\;
C:\Users\shaya\AppData\Local\Programs\Python\Python312\;
C:\Users\shaya\AppData\Local\Programs\Python\Python311\Scripts\;
C:\Users\shaya\AppData\Local\Programs\Python\Python311\;
C:\Users\shaya\AppData\Local\Programs\Python\Python310\Scripts\;
C:\Users\shaya\AppData\Local\Programs\Python\Python310\;
C:\Users\shaya\AppData\Local\Programs\Python\Python39\Scripts\;
C:\Users\shaya\AppData\Local\Programs\Python\Python39\;
C:\Users\shaya\AppData\Local\Programs\Python\Python38\Scripts\;
C:\Users\shaya\AppData\Local\Programs\Python\Python38\;
C:\Users\shaya\AppData\Local\Programs\Python\Launcher\;
```

Each of the `Programs\Python3n\` paths will contain a `python.exe`.

* Running `python` from the command line will run the `python.exe` that was most recently installed. 
* If you `pip install` an executable Python script like `black`, running `black` will start from the top of the list and run the first `Scripts\black` found.
* You will also have the Python Launcher, which you run with `py` at the command line.

If, however, you install Python by downloading and running `*.exe` files from [Download Python \| Python.org](https://www.python.org/downloads/), none of these `Python\Python3n\` or `Python\Python3n\Scripts` entries will be added to your path.

* Running `python` from the command line will launch the Microsoft Store, offering to let you download and install the "missing" Python executable.
* Running a pip-installed script will give you an error message: `The term 'black' is not recognized`.
* You will only have the Python Launcher in your path.

To use the Python Launcher ...

* Run `py` to run the latest Python version.
* Run `py -3.11` to run another version.
* Run `py -m black` to run black from the Scripts folder of the latest Python version.
* Run `py -3.11 -m black` to run black from the Scripts folder of another Python version.
* To run another version by default, create a new User Environment Variable, `PY_PYTHON` and set the value to the default you'd like to run. For example, `3.11`.
* `python` will run as expected from inside a virtual environment.

I prefer the Python-Launcher-only setup, because `python` will *only* work from inside a virtual environment. So, any script you set up to run `python` will only work from a virtual environment, and you can run the latest version from inside a virtual environment by running 'py'.

To accomplish this with a winget install, delete all the `Python\Python3.n` and `Python.n\Scripts` entries from your Path environment variable.

### Older Python Versions

Having the exact Python versions you intend to support installed on your machine is less important than it used to be, because we can test whatever versions we like with continuous integration. So, when it comes to older versions of Python, you don't *have* to compile the latest security release.

If you visit [python.org/downloads](https://www.python.org/downloads/), you will see more recent minor versions of older major versions. For instance, right now, winget installs 3.8.10. The latest (source-only) security release for Python 3.8 is 3.8.20. If you navigate to the install page for one of these source-only releases, you will see a note like this one:

> **No installers**
> According to the release calendar specified in [PEP 569](https://www.python.org/dev/peps/pep-0569/), Python 3.8 is now in the "security fixes only" stage of its life cycle: 3.8 branch only accepts security fixes and releases of those are made irregularly in source-only form until October 2024. Python 3.8 isn't receiving regular bug fixes anymore, and binary installers are no longer provided for it. **Python 3.8.10** was the last full _bugfix release_ of Python 3.8 with binary installers.

... which will direct you to the latest binary (which is probably the binary winget installed). If you're not comfortable *not* having the latest security releases for these older versions, you can just not install those at all and rely on ci for your tests. For what it's worth, my brother works at a company running Python 2.7 in 2024.

# Install Git

```powershell
winget install Git.Git --source winget
```

## Configure Git from PowerShell

Open PowerShell and run the following commands:

```powershell
git config --global user.email "your@email.com"
git config --global user.name "Your Name"
git config --global core.editor "'C:\Program Files\Vim\vim91\vim.exe' -f -i NONE"
git config --global merge.tool vimdiff
git config --global diff.tool vimdiff
git config --global core.excludesFile "$Env:USERPROFILE\.gitignore"
git config --global init.defaultBranch main
```

Don't let the `--global` flag misinform you. These are settings for one user. These commands update a file in your home directory called `.gitconfig`. You can edit this file later or re-run the commands if you don't like what I've put here, but these are the standard settings for Vim users.

If you prefer, you can use `gvimdiff` instead of `vimdiff` for git tools. GVim is a little quicker on Windows than Vim through PowerShell. But usually you're working in Git through the terminal, and your heaviest "tool" usage will be opening up a quick instance for commit messages.

You can also name your default branch whatever you like. If you don't configure it here, you'll get the default `master`. GitHub uses `main`, so if you're using GitHub, you'll save a bit of work by matching what they use there.

### Other Things That Come With Git

The installer will add `git` to your "System environment" Path (not your "User variables" Path).

The Git installer also provides Curl and Bash. Curl will be on your path for plugins like [vim-instant-markdown](https://github.com/instant-markdown/vim-instant-markdown). You can add bash to your path or just create an alias in your PowerShell profile. It's not necessary for Vim, but it's convenient and already installed if you know Bash. Add this to your PowerShell profile.

```powershell
Set-Alias -Name bash -Value 'C:\Program Files\Git\bin\bash.exe'
```

# Install Ripgrep

"Grepping" is a big part of navigating through projects. In Windows, Vim will try to use a grep alternative. I don't remember the name. It works in cmd, but it freezes PowerShell, so we don't want it. Ripgrep is a nice alternative.

```powershell
winget install BurntSushi.ripgrep.MSVC --source winget
```

### Tell Vim to use Ripgrep

Add the following to your `~\vimfiles\vimrc` file. This will tell Vim to use Ripgrep when you use the `:grep` command.

```vim
if has("windows")
    if executable('rg')
        set grepprg=rg\ --vimgrep\ --no-heading
    else
        echoerr "rg not found. Install ripgrep to use :grep"
    endif
endif
```

Once you get everything set up, consider the [ctrl-sf](https://github.com/dyng/ctrlsf.vim) plugin, which will make use of your newly installed and nicely linked ripgrep.

# Install Lua

This step is optional. Lua is required for a few Vim plugins, which you may or may not want to use.

In PowerShell, run

```powershell
winget install DEVCOM.Lua --source winget
```

This will install the file you need (`lua54.dll`) to

```
~\AppData\Local\Programs\Lua\bin\lua54.dll
```

### Tell Vim Where to find Lua

Edit `~\vimfiles\vimrc` and add the following:

```vim
if has("windows")
    var local_programs = expand('$HOME/AppData/Local/Programs')
    execute 'set luadll=' .. local_programs .. '/Lua/bin/lua54.dll'
endif
```

run

```vim
:lua print("test")
```

to make sure everything is set up correctly. As with Python discussed previously, Vim will probably find your Lua without adding this line to the vimrc, but making it explicit can save surprises later on.

# Install Node

This step is optional. If you need Node for [vim-instant-markdown](https://github.com/instant-markdown/vim-instant-markdown) or another plugin, this is a good time to install it. There's not much to it, but it is a JavaScript runtime environment, and some people don't want that weight. Unless you're coming from something extraordinarily light, the editor you were using most likely installed Node without asking you. Your choice.

```powershell
winget install OpenJS.NodeJS.LTS --source winget
```

You run type

```powershell
node -v
```

to check the install.

# Gvim Fullscreen

This step is optional, but if you dislike the toolbar's intruding into your immersive coding experience, you might not feel that way. This executable will allow you to fullscreen gVim.

* Compile from source: [https://github.com/movsb/gvim_fullscreen](https://github.com/movsb/gvim_fullscreen) ... or download [https://github.com/movsb/gvim_fullscreen/releases](https://github.com/movsb/gvim_fullscreen/releases).
* Copy gvimfullscreen.dll to `~/vimfiles/`.

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

This step is optional. It's a fairly big install, but you will need this for some Python libraries like [llama_index](https://github.com/run-llama/llama_index). If you're into things like that, you're going to need it at some point. You can start off by running

```powershell
winget install Microsoft.VisualStudio.2022.BuildTools --source winget
```

This takes several minutes, but only installs the Visual Studio Installer. Once that's done, run the Visual Studio Installer from the Windows menu.

* Click 'Modify'.
* Select "Desktop development with C++".
* Click 'Modify' again.
* You could *probably* go into "Individual Components" and install "C++ CMake tools for Windows" and "Windows 11 SDK" only, but the entire "Workload" is only 1.75GB and it's not worth the hassle to figure out what you need and what you don't.
* There's also a way, I'm sure to [Use command-line parameters to install Visual Studio](https://learn.microsoft.com/en-us/visualstudio/install/use-command-line-parameters-to-install-visual-studio?view=vs-2022#use-winget-to-install-or-modify-visual-studio), but I'm not too proud to use the gui installer.

# Install Lazygit

This step is optional, but [Lazygit](https://github.com/jesseduffield/lazygit/) is fun and cool and useful. Like all Git interfaces, it's got [issues](https://github.com/jesseduffield/lazygit/issues)---as I write this, 666 open issues---but don't let the open issues put you off. As I said (and if you'll excuse a little fun with the coincidence), it's *the nature of the beast*---which may be a big part of the reason you're installing Vim in the first place (fewer interfaces).

```powershell
winget install JesseDuffield.lazygit --source winget
```

Close and restart your Windows Terminal, navigate to a Git project, and type `lazygit` to have a look.
