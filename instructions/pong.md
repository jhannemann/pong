# Writing a Pong Clone with Python and pygame

This tutorial will walk you through the creation of a clone
of the classic video game [Pong](https://en.wikipedia.org/wiki/Pong),
using the [Python](https://python.org) programming language
and the [pygame](https://pygame.org) game engine.

## Installing Python and pygame

On Windows or MacOS,
download the latest version of Python 3
from the [Python website](https://www.python.org/downloads/).
On Linux, install it using your distibution's package manager.

pygame installation is done via `pip`,
the *Package Installer for Python*.
To make sure that pygame works with Python 3
and also works with high-resolution screens
(such as a Mac Retina Display),
we will install the latest beta version for pygame 2.
As of this writing, the pygame developers are close
to officially release pygame 2.0,
so we should not run into any issues with the beta version.

### Windows

On Windows, open up a command line or the PowerShell.
Make sure you have Python3 installed by typing
```
py --version
```
The answer should be something like `Python 3.8.3`.
Install pygame with the following command:
```
py -m pip install -U 'pygame>=2.0.0-dev10' --user
```

### MacOS and Linux

On a Mac or Linux PC,
open up the Terminal app.
Install pygame with the following command:
```
python3 -m pip install -U 'pygame>=2.0.0-dev10' --user
```

## Coding Guidelines

Every programming language has its preferred way of writing code in it.
For Python,
these preferences are written down in the
[Python Enhancement Proposal Number 8](https://www.python.org/dev/peps/pep-0008/),
or PEP-8 for short.
The code we will write will be PEP-8 compliant.
I encourage you to review that document,
as many of the principles mentioned also apply to many other programming languages,
and having a consistent coding style will make you a better developer.

## IDLE

We will be using Pyhon's builtin *Integrated Development Environment* (IDE).
Its official name is the *Integrated Development and Learning Environment*,
or IDLE.
You should be able to start it from your operating system's search bar
or program launcher,
once Python is installed.
IDLE is a basic tool that is more than sufficient for our code,
but if you plan to use Python for more elaborate projects,
check out [PyCharm](https://www.jetbrains.com/pycharm/).
PyCharm comes in a free community edition,
which can handle even large Python projects quite nicely.

## License

SPDX-License-Identifier: CC-BY-SA-4.0
