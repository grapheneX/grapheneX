![grapheneX](https://user-images.githubusercontent.com/24392180/60434254-65ed3e00-9c0f-11e9-8b73-73f9a1b25f60.png)

# grapheneX [![Release](https://img.shields.io/github/release/grapheneX/grapheneX.svg?style=flat-square)](https://github.com/grapheneX/grapheneX/releases)

[![Issues](https://img.shields.io/github/issues/grapheneX/grapheneX.svg?style=flat-square)](https://github.com/grapheneX/grapheneX/issues)
[![Pull Requests](https://img.shields.io/github/issues-pr/grapheneX/grapheneX.svg?style=flat-square)](https://github.com/grapheneX/grapheneX/pulls)
[![Stars](https://img.shields.io/github/stars/grapheneX/grapheneX.svg?style=flat-square)](https://github.com/grapheneX/grapheneX/stargazers)
[![Forks](https://img.shields.io/github/forks/grapheneX/grapheneX.svg?style=flat-square)](https://github.com/grapheneX/grapheneX/network)
[![License](https://img.shields.io/github/license/grapheneX/grapheneX.svg?style=flat-square)](./LICENSE)

> In computing, hardening is usually the process of securing a system by reducing its surface of vulnerability, which is larger when a system performs more functions; in principle a single-function system is more secure than a multipurpose one. Reducing available ways of attack typically includes changing default passwords, the removal of unnecessary software, unnecessary usernames or logins, and the disabling or removal of unnecessary services.

Although the current technology tries to design systems as safe as possible, security flaws and situations that can lead to vulnerabilities caused by unconscious use and missing configurations still exist.
The user must be knowledgeable about the technical side of system architecture and should be aware of the importance of securing his/her system from vulnerabilities like this. 
Unfortunately, it's not possible to know all the details about hardening and necessary commands for every ordinary user and the hardening remains to be a technical issue due to the difficulty of understanding operating system internals. 
Therefore there are hardening checklists that contain various commands and rules of the specified operating system available such as [trimstray/linux-hardening-checklist](https://github.com/trimstray/linux-hardening-checklist) & [Windows Server Hardening Checklist](https://www.upguard.com/blog/the-windows-server-hardening-checklist) on the internet for providing a set of commands with their sections and of course simplifying the concept for the end user.
But still, the user must know the commands and apply the hardening manually depending on the system. That's where the `grapheneX` exactly comes in play.

> The project name is derived from the 'graphene'. Graphene is a one-atom-thick layer of carbon atoms arranged in a hexagonal lattice. In proportion to its thickness, it is about 100 times stronger than the strongest steel.

`grapheneX` project aims to provide a framework for securing the system with hardening commands automatically. 
It's designed for the end user as well as the Linux and Windows developers due to the interface options. (interactive shell/web interface) 
In addition to that, `grapheneX` can be used to secure a web server/application.

Hardening commands and the scopes of those commands are referred to `modules` and the `namespaces` in the project. 
Additionally, it's possible to add, edit or remove modules and namespaces. 
Also, the hardening operation can be automated with the presets that contain a list of modules.

Currently, grapheneX support the hardening sections below. Each of these namespaces contains more than one module.

• Firewall  
• User   
• Network   
• Services   
• Kernel   
• Filesystem  
• Other

## Installation

### Dependencies

* [Flask-SocketIO](https://flask-socketio.readthedocs.io/en/latest/)
  *  [Flask](http://flask.pocoo.org/)
* [coloredlogs](https://pypi.org/project/coloredlogs/)
* [terminaltables](https://pypi.org/project/terminaltables/)
* [PyInquirer](https://pypi.org/project/PyInquirer/)

### Package Installation

Pip:

```
pip install -r requirements.txt
python grapheneX.py
```

Pipenv:

```
pipenv install
pipenv run python grapheneX.py
```

## Usage

### Command Line Arguments

```
usage: grapheneX.py [-h] [-v] [-w] [--open] [host:port]

grapheneX | Automated System Hardening Framework

positional arguments:
  host:port      host and port to run the web interface

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show version information
  -w, --web      run the grapheneX web server
  --open         open browser on web server start
```

### Interactive Shell

### Web Interface

## Commands

### help

### list

### switch

### use

### info

### harden

### back

### search

### manage

### web

### clear

Clear terminal

### exit

Exit interactive shell

## Web

## Examples

## Screenshots

## TODO(s)

## Contribution

For contributing to this project, see [CONTRIBUTING.md](./CONTRIBUTING.md)

## Sponsors

We don't have any sponsors yet. Contact us with email if you want to help us improve the project.

## License

GNU General Public License v3.0 ([gpl](https://www.gnu.org/licenses/gpl.txt))

## Credit

Copyright (C) 2019 by [GrapheneX Team](https://github.com/orgs/grapheneX/people)