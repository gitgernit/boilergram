# Contributing

## Introduction

### Thank you!
I am thankful to you as to a (potential) contributor, and 
I am glad that you are reading this. Boilergram 
was and is being made to help developers develop, and helping 
each-other is what we should all aspire to.

### Following contribution rules & standards
Following the guidelines will generally ease the contributing 
process. If you meet the defined criteria, the chance that 
your pull request will be declined or sent to code review is 
much less. Community spirit `await`s!

### What kinds of contributions are welcome
Almost anything! Whether it's the light bulb that got you here 
with a feature request, an issue that you stumbled upon while 
using boilergram (eh!) or any other enhancement that you 
believe will help the project - take your shot!

### What kinds of contributions are not welcome
Any contributions that are in fact not contributions. 
If you are having trouble working with the framework, 
yet you are not sure that the occurring behaviour is 
unintended - please, ask for help in other places
(i.e. official telegram channel [@boilergram](https://t.me/boilergram))

## Ground Rules

### Responsibilities
The essential responsibility of a contributor lies in the 
[Code Of Conduct](CODE_OF_CONDUCT.md). If you haven't read it 
yet - please, do.

You should also meet the technical responsibilities, rules and
standards. Here are some:
- Always lint, format and test your code before pushing
- Follow the commit convention, try using gitmojis
- Write concise yet meaningful commit messages
- Follow gitflow! Use the issue tracker to declare 
bugs \ features, separate branches for their fulfillment.
- Draft pull requests!

## Your First Contribution

You can start by looking around the project. Check open PRs, 
the issue tracker (caution with the labels!), hover through
the codebase, get comfortable!  
If you're confused - feel free to ask for help! Everyone is a 
beginner at first, being a newbie-friendly community is what 
boilergram encourages everyone to do.  
*[First time contributing?](https://www.firsttimersonly.com/)*

# Getting started

## Prerequisites
It is suggested you use an IDE or a text editor of your choice 
when working with boilergram.
1. Install the latest python version  
    You can use a package manager of your choice or get 
    the installer from [the official python site](https://www.python.org),
    e.g.:  
    ```shell
    pacman -S python
    ```
2. Clone the repository
    ```git
    git clone https://github.com/gitgernit/boilergram.git
    ```
    ```shell
    cd boilergram
    ```

3. Install uv and boilergram's dependencies
    ```shell
    pip install uv
    ```
    ```shell
    uv sync
    ```

4. Set up pre-commit hooks
    ```shell
    pre-commit install
    ```
   
Now you're all set!

## Submitting a bug or a feature
1. Open an issue, follow the template. Done

### Fixing a bug or implementing a feature
This applies to any kinds of fixes & enhancements.
Even if your change is a one-liner, you should still
follow these steps.

1. Open an issue, follow the template, note that you
wish to be the assignee
2. Fork the project
3. Create a branch
4. Fix the bug, obviously
5. Create a pull request, pass the code-review

## Community
Currently, the only official place representing boilergram and 
its community is the official telegram channel - 
[@boilergram](https://t.me/boilergram). 

## Bonus

### Preferred Code Style
We try to err on the side of bug-prone, well-formatted code.
All the formatting rules are present in boilergram's linters 
configurations. You can read about most of the rules from 
[.ruff.toml](.ruff.toml) on [astral](https://docs.astral.sh/ruff/rules/),
[.isort.cfg](.isort.cfg) - from [pycqa](https://pycqa.github.io/isort/)

### Preferred commit style
Gitmojis combined with the traditional commit convention makes 
beauty. In example:  
```
:sparkles:feat(scope): update CONTRIBUTING.md

added an example of a commit
```

### Preferred labeling style
Here are some branches:
```
feature/cli
feature/contrib-guidelines
fix/init-bottleneck
fix/issue-13
```

Here are some pull requests:
```
feature/linting - Linters and their configurations
```

### That's it
I'm done
