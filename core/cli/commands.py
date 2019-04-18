from core.utils.logcl import GraphenexLogger
from core.cli.help import Help
from core.utils.helpers import check_os
import core.hrd.linux as linux_harden_module
import core.hrd.win as win_harden_module

from asciitree import LeftAligned
from collections import OrderedDict as OD
import os

from pprint import pprint

logger = GraphenexLogger(__name__, 'DEBUG')


class ShellCommands(Help):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)
        # Create ascii tree
        self.base_tree = {'MODULES': dict(linux={}, windows={})}
        self.harden_tree = self.base_tree['MODULES']
        for k in linux_harden_module.MODULES.keys():
            self.harden_tree['linux'].update({k: dict((j.__name__, dict()) for j in linux_harden_module.MODULES[k])})

        for k in win_harden_module.MODULES.keys():
            self.harden_tree['windows'].update({k: dict((j.__name__, dict()) for j in win_harden_module.MODULES[k])})

        self.tree = LeftAligned()

    def do_switch(self, arg):
        """Change module"""

        # TODO: Check control
        self.harden_str = arg

    def do_search(self, arg):
        if arg:
            try:
                md = {arg: self.harden_tree[arg]}
                print(self.tree(md))
            except KeyError:
                print(f"Module not found '{arg}'")
                logger.debug(f"Module not found '{arg}'. Check __init__.py")
        else:
            print(self.tree(self.base_tree))

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

        