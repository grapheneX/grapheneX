from core.utils.logcl import GraphenexLogger
from core.cli.help import Help
from core.utils.helpers import check_os
import core.hrd.linux as linux_harden_module
import core.hrd.win as win_harden_module

from asciitree import LeftAligned
import os
import re


logger = GraphenexLogger(__name__)


"""
Note
-----
How to add harden module:
    Move hardenmodule file to `core/hrd/[linux|win]`. Eg: `core/hrd/linux/network.py`
    then register all classes that you write in the `__init__.py` like I did. 
"""

class ShellCommands(Help):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)

        # Create tree
        # for asciitree module. More: https://pypi.org/project/asciitree/
        self.base_tree = {'MODULES': dict(linux={}, windows={})}
        self.harden_tree = self.base_tree['MODULES']
        self.current_tree = self.harden_tree
        for k in linux_harden_module.MODULES.keys():
            self.harden_tree['linux'].update(
                {k: dict((j.__name__, dict()) for j in linux_harden_module.MODULES[k])})

        for k in win_harden_module.MODULES.keys():
            self.harden_tree['windows'].update(
                {k: dict((j.__name__, dict()) for j in win_harden_module.MODULES[k])})

        self.tree = LeftAligned()

    def do_switch(self, arg):
        """Change module"""
        if arg:
            try:
                va_arg = [re.sub(r"\s+", "", i, flags=re.UNICODE)
                          for i in arg.split('>')]  # Skip whitespace

                if (len(va_arg) == 1):  # Only one arg, like: `switch windows`
                    va_arg = va_arg[0]
                    try:
                        self.current_tree = {
                            f"{va_arg}": self.current_tree[va_arg]}
                    except KeyError:
                        control = self.current_tree.get('linux')
                        logger.debug(f"control: {control}")
                        if self.current_tree:
                            self.current_tree = {
                                f"{va_arg}": self.current_tree.get('windows').get(va_arg)}
                        else:
                            self.current_tree = {
                                f"{va_arg}": self.current_tree.get('linux').get(va_arg)}

                    self.harden_str = va_arg
                else:
                    # Multiple arg, like : `switch linux > network`
                    self.current_tree = self.current_tree[va_arg[0]][va_arg[1]]
                    self.harden_str = " > ".join(va_arg)
            except KeyError:
                print(f"Module not found '{arg}'")
                logger.debug(
                    f"Module not found '{arg}'. Maybe forgot module name register to __init__.py.")

    def do_search(self, arg):
        "Search available submodules"

        if arg:
            try:
                va_arg = [re.sub(r"\s+", "", i, flags=re.UNICODE)
                          for i in arg.split('>')]  # skip whitespace
                logger.debug(va_arg)

                if (len(va_arg) == 1):
                    va_arg = va_arg[0]
                    ####### search command custom args #######
                    if va_arg == '/all':
                        print()
                        print(self.tree(self.base_tree))
                        print()
                        return  # End arg
                    ######## End #######
                    md = {f"{va_arg}": self.current_tree[va_arg]}
                else:
                    md = {f"{va_arg[0]}": {
                        f"{va_arg[1]}": self.current_tree[va_arg[0]][va_arg[1]]}}

                print()
                print(self.tree(md))
                print()

            except KeyError:
                print(f"Module not found '{arg}'")
                logger.debug(
                    f"Module not found '{arg}'. Maybe forgot module name register to __init__.py.")
        else:
            print()
            print(self.tree(self.current_tree)
                  if self.harden_str else self.tree(self.base_tree))
            print()

    def do_exit(self, arg):
        "Exit interactive shell"

        logger.info('Exit shell')
        print("Bye")
        return True

    def do_clear(self, arg):
        """Clear terminal"""

        os.system("cls" if check_os() else "clear")

    def default(self, line):
        print("Command not found!")
