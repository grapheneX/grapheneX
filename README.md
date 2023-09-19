![grapheneX](https://socialify.git.ci/grapheneX/grapheneX/image?description=1&font=Raleway&forks=1&issues=1&language=1&logo=https%3A%2F%2Fraw.githubusercontent.com%2FgrapheneX%2FgrapheneX%2Fmaster%2Fgraphenex%2Fcore%2Fweb%2Fstatic%2Fimages%2Fgraphenex_logo_white.png&owner=1&pulls=1&stargazers=1&theme=Dark)

# grapheneX [![Release](https://img.shields.io/github/release/grapheneX/grapheneX.svg?style=flat-square)](https://github.com/grapheneX/grapheneX/releases) [![License](https://img.shields.io/github/license/grapheneX/grapheneX.svg?style=flat-square)](./LICENSE)

> In computing, hardening is usually the process of securing a system by reducing its surface of vulnerability, which is larger when a system performs more functions; in principle a single-function system is more secure than a multipurpose one. Reducing available ways of attack typically includes changing default passwords, the removal of unnecessary software, unnecessary usernames or logins, and the disabling or removal of unnecessary services.

`grapheneX` project aims to provide a framework for securing the system with hardening commands automatically.
It's designed for the end user as well as the Linux and Windows developers due to the interface options. (interactive shell/web interface)
In addition to that, `grapheneX` can be used to secure a web server/application.

> The project name is derived from 'graphene'. Graphene is a one-atom-thick layer of carbon atoms arranged in a hexagonal lattice. In proportion to its thickness, it is about 100 times stronger than the strongest steel.

Hardening commands and the scopes of those commands are referred to `modules` and the `namespaces` in the project.
They exist at the `modules.json` file after installation. (`$PYPATH/site-packages/graphenex/modules.json`)
Additionally, it's possible to add, edit or remove modules and namespaces.
Also, the hardening operation can be automated with the presets that contain a list of modules.

Currently, grapheneX supports the hardening sections below. Each of these namespaces contains more than one module.

• Firewall  
• User  
• Network  
• Services  
• Kernel  
• Filesystem  
• Other

Listen to The Python Podcast.\_\_init\_\_: [Automate Your Server Security With GrapheneX - Episode 237](https://www.pythonpodcast.com/graphenex-server-security-episode-237/)

## Installation

You can install `grapheneX` with `pip`. Usually this is the easiest way:

```
pip install graphenex
```

Or if you get an error try:

```
python3 -m pip install graphenex
```

Additionally, [poetry](https://python-poetry.org/) can be used for development:

```
poetry install        # install the dependencies
poetry run grapheneX  # run grapheneX
```

### Dependencies

- [Flask-SocketIO](https://flask-socketio.readthedocs.io/en/latest/)
  - [Flask](http://flask.pocoo.org/)
- [coloredlogs](https://pypi.org/project/coloredlogs/)
- [colorama](https://pypi.org/project/colorama/)
- [terminaltables](https://pypi.org/project/terminaltables/)
- [PyInquirer](https://pypi.org/project/PyInquirer/)

## Usage

### Command Line Arguments

```
usage: grapheneX [-h] [-v] [-w] [--open] [host:port]
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

Execute the `grapheneX` command in order to start the interactive shell.

![GrapheneX Interactive Shell](https://user-images.githubusercontent.com/24392180/61892273-16e7af80-af14-11e9-91d8-8c7682439f06.gif)

• Animated gifs and screenshots added for demonstration and include the test execution of the unversioned grapheneX. Use `grapheneX` or `python -m graphenex` command for the execution.  
• grapheneX currently supports [Python3.10](https://www.python.org/)

### Web Interface

Execute the `grapheneX` with the `-w` or `--web` argument in order to start the web server.

![Starting the Web Server](https://user-images.githubusercontent.com/24392180/61898426-f292cf80-af21-11e9-9edc-21f0351bbf5b.gif)

• Web interface has the authentication system that requires an `access token`. Once the user verifies her/his identity with the given token at the shell, grapheneX creates a session for further use.

![GrapheneX Web Interface I](https://user-images.githubusercontent.com/24392180/61898886-fd019900-af22-11e9-9d1e-e2a58bee6651.gif)

![GrapheneX Web Interface II](https://user-images.githubusercontent.com/24392180/60525198-9bb92200-9cf6-11e9-80c6-9b69b5d10c81.gif)

• The default host and port value are `localhost:8080`. It can be changed via the `host:port` argument as shown below.

```
python3 -m graphenex -w 192.168.1.36:8090
```

• Use `--open` argument to open the browser after the server start.

```
python3 -m graphenex -w --open
```

## CLI Commands

| Command | Description                                                                   |
| ------- | ----------------------------------------------------------------------------- |
| back    | Go back from namespace or module                                              |
| clear   | Clear the terminal                                                            |
| exit    | Exit interactive shell                                                        |
| harden  | Execute the hardening command                                                 |
| help    | List available commands with "help" or show detailed help with "help `<cmd>`" |
| info    | Show information about the module                                             |
| list    | List available hardening modules                                              |
| manage  | Add, edit or delete module                                                    |
| preset  | Show/execute the hardening module presets                                     |
| search  | Search for modules                                                            |
| switch  | Switch between modules or namespaces                                          |
| use     | Use a hardening module                                                        |
| web     | Start the grapheneX web server                                                |

### help

`help` or `?` shows the commands list above.  
`help [CMD]` shows the detailed usage of given command.

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

Executes the hardening command of the selected module.

![Harden Command](https://user-images.githubusercontent.com/24392180/60531788-67e4f900-9d04-11e9-8960-2d2f2a7289f0.gif)

### preset

grapheneX has presets that contain particular modules for automating the hardening operation. Presets can be customized with the `modules.json` file, and they can contain any supported module. `preset` command shows the available module presets and `preset [PRESET]` runs the hardening commands in a preset.

![Show Presets](https://user-images.githubusercontent.com/24392180/60548388-a097c900-9d2a-11e9-8927-bbbd90493430.gif)

An example `preset` command output is shown above. Below, a preset that contains 2 modules is selected and hardening modules executed.

![Preset Command](https://user-images.githubusercontent.com/24392180/60548929-0cc6fc80-9d2c-11e9-9bff-01882feb6b9f.gif)

`preset` command supports autocomplete for preset names. Also, it supports an option for asking permission between each hardening command execution so that the user knows what he/she is doing.

• Adding module presets

Presets are stored in the `presets` element inside the `modules.json` file. This JSON file can be edited for updating the presets.

```
"presets": [
        {
            "name": "Preset_1",
            "modules": [
                "namespace1/Module_Name1",
                "namespace2/Module_Name2",
            ],
            "target_os": "linux/win"
        },
        {
            "name": "Preset_2",
            "modules": [
                "namespace/All"
            ],
            "target_os": "linux/win"
        }
    ]
```

`namespace/All` means every hardening command in that `namespace` will be executed.

### search

```
search [QUERY]
```

![Search Command](https://user-images.githubusercontent.com/24392180/60532081-26a11900-9d05-11e9-87da-ee7eefd3ab90.gif)

### manage

`manage` command allows to add, edit or remove modules.

• Adding modules with `manage`

Follow the instructions for adding a new module. Choose the 'new' option in the namespace prompt for creating a new namespace.

![Adding Module](https://user-images.githubusercontent.com/24392180/60544556-b1900c80-9d21-11e9-8013-69be929fdf53.gif)

• Adding modules manually

grapheneX stores the modules and namespaces in `modules.json` file. It will show up as a new module when a new element is created in this JSON file. An example element is given below.

```
"namespace": [
        {
            "name": "Module_Name",
            "desc": "This is the module description.",
            "command": "echo 'hardening command'",
            "require_superuser": "True/False",
            "target_os": "linux/win"
        }
    ]
```

It's recommended to add modules from CLI or the Web interface other than editing the `modules.json` file.

• Editing modules

Choose the `edit` option after the `manage` command for the editing the module properties.

![Editing Module](https://user-images.githubusercontent.com/24392180/60545208-30d21000-9d23-11e9-8b5d-e85a52521180.gif)

Or edit the `modules.json` manually.

• Removing modules

Choosing the `remove` option in the `manage` menu will be enough for removing the specified module. It's also possible to remove the module from `modules.json` manually.

![Removing Module](https://user-images.githubusercontent.com/24392180/60545589-18aec080-9d24-11e9-9e3f-2385f05ecf09.gif)

### web

Starts the grapheneX web server with the optional `host:port` argument.

```
web [host:port]
```

![Web Command](https://user-images.githubusercontent.com/24392180/60546423-f027c600-9d25-11e9-8d45-e9cd9373d9bd.gif)

### back

Go back from selected namespace or module.

### clear

Clear terminal

### exit

Exit interactive shell

## Web

Most of the command line features are accessible with the Web interface.

### Namespaces & Modules

It's easy to switch between namespaces and see details of modules.

![Namespaces and Modules](https://user-images.githubusercontent.com/24392180/60549923-02f2c880-9d2f-11e9-9ee2-b3f58afeb5fd.gif)

### Hardening

Just click `run` under the module properties for executing the hardening command.

![Hardening](https://user-images.githubusercontent.com/24392180/60551119-f2dce800-9d32-11e9-9e4b-126354778e9f.gif)

### Adding Modules

There's a menu available in the web interface for adding new modules.

![Adding Modules](https://user-images.githubusercontent.com/24392180/60551262-6c74d600-9d33-11e9-8c3e-f553fafdda74.gif)

### System Monitor

It's possible to display various system information such as disk usage and network state at the Web interface.

![System Monitor](https://user-images.githubusercontent.com/24392180/64130757-12dd6600-cdcd-11e9-9be8-39395e104974.gif)

## Docker

### Building the image

```sh
docker build -f docker/Dockerfile -t graphenex .
```

### Running the container

```sh
docker run -it --rm --name graphenex -p 8080:8080 --privileged graphenex
```

## Screenshots

![Screenshot I](https://user-images.githubusercontent.com/24392180/60615641-47866e80-9dd8-11e9-92fe-dfa8874db8fd.jpg)

![Screenshot II](https://user-images.githubusercontent.com/24392180/60601258-7e4d8c00-9dba-11e9-93e1-96411b76b462.png)

![Screenshot III](https://user-images.githubusercontent.com/24392180/60625283-9be51a80-9de7-11e9-99ea-46875d8b3ed8.JPG)

![Screenshot IV](https://user-images.githubusercontent.com/24392180/60625314-bae3ac80-9de7-11e9-98ef-e5fa69c3be38.JPG)

![Screenshot V](https://user-images.githubusercontent.com/24392180/60625373-eb2b4b00-9de7-11e9-9e9a-ab1869af9b1a.JPG)

## TODO(s)

- Add new modules for Linux and Windows.

## Contributing

For contributing to this project, see [CONTRIBUTING.md](./CONTRIBUTING.md)

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/orhun"><img src="https://avatars1.githubusercontent.com/u/24392180?v=4?s=100" width="100px;" alt="orhun"/><br /><sub><b>orhun</b></sub></a><br /><a href="https://github.com/grapheneX/grapheneX/commits?author=orhun" title="Code">💻</a> <a href="https://github.com/grapheneX/grapheneX/commits?author=orhun" title="Documentation">📖</a> <a href="#projectManagement-orhun" title="Project Management">📆</a> <a href="#question-orhun" title="Answering Questions">💬</a> <a href="#ideas-orhun" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/grapheneX/grapheneX/pulls?q=is%3Apr+reviewed-by%3Aorhun" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/bufgix"><img src="https://avatars1.githubusercontent.com/u/22038798?v=4?s=100" width="100px;" alt="Faruk"/><br /><sub><b>Faruk</b></sub></a><br /><a href="https://github.com/grapheneX/grapheneX/commits?author=bufgix" title="Code">💻</a> <a href="#design-bufgix" title="Design">🎨</a> <a href="#platform-bufgix" title="Packaging/porting to new platform">📦</a> <a href="#ideas-bufgix" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/grapheneX/grapheneX/pulls?q=is%3Apr+reviewed-by%3Abufgix" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/EnesOkutan"><img src="https://avatars0.githubusercontent.com/u/36725317?v=4?s=100" width="100px;" alt="EnesOkutan"/><br /><sub><b>EnesOkutan</b></sub></a><br /><a href="https://github.com/grapheneX/grapheneX/commits?author=EnesOkutan" title="Code">💻</a> <a href="#ideas-EnesOkutan" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/grapheneX/grapheneX/pulls?q=is%3Apr+reviewed-by%3AEnesOkutan" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/afk"><img src="https://avatars0.githubusercontent.com/u/22278039?v=4?s=100" width="100px;" alt="Efe Aydın"/><br /><sub><b>Efe Aydın</b></sub></a><br /><a href="https://github.com/grapheneX/grapheneX/commits?author=afk" title="Code">💻</a> <a href="#ideas-afk" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/grapheneX/grapheneX/pulls?q=is%3Apr+reviewed-by%3Aafk" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ibanez75612"><img src="https://avatars0.githubusercontent.com/u/26774223?v=4?s=100" width="100px;" alt="ibanez75612"/><br /><sub><b>ibanez75612</b></sub></a><br /><a href="https://github.com/grapheneX/grapheneX/commits?author=ibanez75612" title="Code">💻</a> <a href="#platform-ibanez75612" title="Packaging/porting to new platform">📦</a> <a href="https://github.com/grapheneX/grapheneX/pulls?q=is%3Apr+reviewed-by%3Aibanez75612" title="Reviewed Pull Requests">👀</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://www.emperorfederico.info"><img src="https://avatars1.githubusercontent.com/u/37400853?v=4?s=100" width="100px;" alt="Emperor  Federico"/><br /><sub><b>Emperor  Federico</b></sub></a><br /><a href="https://github.com/grapheneX/grapheneX/commits?author=emperorfederico" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/kondanta"><img src="https://avatars1.githubusercontent.com/u/16501501?v=4?s=100" width="100px;" alt="Taylan"/><br /><sub><b>Taylan</b></sub></a><br /><a href="#infra-kondanta" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/zero77"><img src="https://avatars3.githubusercontent.com/u/16563034?v=4?s=100" width="100px;" alt="zero77"/><br /><sub><b>zero77</b></sub></a><br /><a href="https://github.com/grapheneX/grapheneX/commits?author=zero77" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://privateger.me/"><img src="https://avatars0.githubusercontent.com/u/29523614?v=4?s=100" width="100px;" alt="Marc"/><br /><sub><b>Marc</b></sub></a><br /><a href="#content-PerhapsSomeone" title="Content">🖋</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://mercode.org"><img src="https://avatars1.githubusercontent.com/u/40173707?v=4?s=100" width="100px;" alt="Tan Siret G. AKINCI"/><br /><sub><b>Tan Siret G. AKINCI</b></sub></a><br /><a href="https://github.com/grapheneX/grapheneX/commits?author=Yutyo" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/jxd1337"><img src="https://avatars.githubusercontent.com/u/138708600?v=4?s=100" width="100px;" alt="jxd1337"/><br /><sub><b>jxd1337</b></sub></a><br /><a href="https://github.com/grapheneX/grapheneX/commits?author=jxd1337" title="Code">💻</a> <a href="#ideas-jxd1337" title="Ideas, Planning, & Feedback">🤔</a> <a href="https://github.com/grapheneX/grapheneX/commits?author=jxd1337" title="Documentation">📖</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

## Sponsors

We don't have any sponsors yet. Contact us with email if you want to help us improve the project.

## License

GNU General Public License v3.0 ([gpl](https://www.gnu.org/licenses/gpl.txt))
