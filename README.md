# boilergram

![GitHub License](https://img.shields.io/github/license/gitgernit/boilergram)
![PyPI - Version](https://img.shields.io/pypi/v/boilergram)
![PyPI - Downloads](https://img.shields.io/pypi/dm/boilergram)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/boilergram)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/gitgernit/boilergram/test-python-code.yml)
![Codecov](https://img.shields.io/codecov/c/github/gitgernit/boilergram)



## Introduction

### What is boilergram?
boilergram is a framework that helps you build your telegram 
bots using **[aiogram](https://github.com/aiogram/aiogram)**!


### Why should I use boilergram?
boilergram enforces and looks after a django-like structure 
of your project. Thus, you can focus on writing actual code 
and not worry about your project getting messy & unextendable.

### What boilergram is and what boilergram isn't
boilergram is just an additional layer between the developer and
the actual framework communicating with Telegram. boilergram does
not in any way modify **[aiogram](https://github.com/aiogram/aiogram)**
behaviour nor does it change the actual behaviour of your bot.

## Getting started

### Requirements
- Python >=3.11
- git

### Installation
Install the package using a package manager of your choice.
It is recommended that you use a virtual environment 
or any other dependency isolation tool when doing so.
E.g.:
```shell
pip install boilergram
```

### Usage
After installing the package you can jumpstart your 
**[aiogram's](https://github.com/aiogram/aiogram)**
project using the `init` command:
```shell
boilergram init
```
boilergram will prompt you the required information and create 
your project. The project's tree would look like this:
```
mybot/
├── manage.py
└── mybot/
    ├── __init__.py
    └── settings.py
```

Fill the mandatory variables (i.e. bot api token) in the 
`settings.py` file, then start your freshly-baked bot 
using `manage.py`!
```shell
python myproject/manage.py runbot
```

That's it for the basic usage. For more info on managing your 
project and creating your own apps, refer to the official 
documentation.

## Other info

### Contributing
Refer to the [Contributing Guidelines](CONTRIBUTING.md)

### License
[MIT](LICENSE)

### Sources
boilergram is **HEAVILY** backed by **[aiogram](https://github.com/aiogram/aiogram)**.
Leave them a star.
