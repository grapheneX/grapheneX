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
```
```
positional arguments:
  host:port      host and port to run the web interface

optional arguments:
  -h, --help     show this help message and exit
  -v, --version  show version information
  -w, --web      run the grapheneX web server
  --open         open browser on web server start
```

### Interactive Shell

Execute the `grapheneX.py` in order to start the interactive shell.

![GrapheneX Interactive Shell](https://user-images.githubusercontent.com/24392180/60462623-7a9ef580-9c52-11e9-8baf-039c2e97669d.gif)

• grapheneX currently supports [Python3.7](https://www.python.org/)   
• Project's some functions (such as hardening) might not work without root access. So consider running the grapheneX with sudo/administrative access.

### Web Interface

Execute the `grapheneX.py` with the `-w` or `--web` argument in order to start the web server. 

![Starting the Web Server](https://user-images.githubusercontent.com/24392180/60523549-99a19400-9cf3-11e9-85eb-d89cfb083056.gif)

![GrapheneX Web Interface](https://user-images.githubusercontent.com/24392180/60525198-9bb92200-9cf6-11e9-80c6-9b69b5d10c81.gif)


• The default host and port value are `0.0.0.0:8080`. It can be changed via the `host:port` argument as shown below.

```
python grapheneX.py -w 192.168.1.36:8090
```

• Use `--open` argument to open the browser after the server start. 

```
python grapheneX.py -w --open
```

## CLI Commands

| Command 	| Description                                                                 	|
|---------	|-----------------------------------------------------------------------------	|
| back    	| Go back from namespace or module                                            	|
| clear   	| Clear the terminal                                                          	|
| exit    	| Exit interactive shell                                                      	|
| harden  	| Execute the hardening command                                               	|
| help    	| List available commands with "help" or show detailed help with "help <cmd>" 	|
| info    	| Show information about the module                                           	|
| list    	| List available hardening modules                                            	|
| manage  	| Add, edit or delete module                                                  	|
| preset  	| Show/execute the hardening module presets                                   	|
| search  	| Search for modules                                                          	|
| switch  	| Switch between modules or namespaces                                        	|
| use     	| Use a hardening module                                                      	|
| web     	| Start the grapheneX web server                                              	|

### help

`help` or `?` shows the commands list above.  
`help [CMD]` shows the detailed usage of given command.

![Help Command](https://user-images.githubusercontent.com/24392180/60530004-8648f580-9d00-11e9-82b7-7adc05f94a42.gif)


### list

Show the available modules in a table.
For example:

![List Command](https://user-images.githubusercontent.com/24392180/60528104-5e579300-9cfc-11e9-9a01-ac827fd365b1.gif)

### switch

`switch` command can be used to switch to a namespace or use a module. It's helpful if you want to see a list of modules in a namespace.

```
switch [NAMESPACE]
```

![Switch Command](https://user-images.githubusercontent.com/24392180/60528986-46810e80-9cfe-11e9-9870-00333657fdee.gif)

• Supports autocomplete for namespaces.

Also, using the `switch` command like this is possible:

```
switch [NAMESPACE]/[MODULE]
```

It's the equivalent of the `use` command in this situation.

### use

Serves the purpose of selecting a hardening module.

```
use [MODULE]
```

![Use Command](https://user-images.githubusercontent.com/24392180/60530449-69f98880-9d01-11e9-93a9-4f612e4ed7ad.gif)

• Supports autocomplete for modules.

### info

Shows information (namespace, description, OS command) about the selected module.

![Info Command](https://user-images.githubusercontent.com/24392180/60531173-02dcd380-9d03-11e9-9410-a59e6ed3d5a4.gif)

### harden

### preset

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