#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from cmd import Cmd
from core.cli.commands import ShellCommands
from core.utils.helpers import get_modules

class Shell(ShellCommands, Cmd):
    """Interactive Shell constructor class"""
    namespace = ""
    module = ""
    modules = get_modules()
    intro = "Welcome to the grapheneX interactive shell. " + \
            "Type \"help\" or \"?\" to list commands."

    @property
    def prompt(self):
        """Set prompt according to the current module and namespace"""
        prompt_str = ""
        if self.namespace:
            prompt_str = prompt_str + ":" + self.namespace
        if self.module:
            prompt_str = prompt_str + ":" + self.module
        return f"[gX{prompt_str}]> "

def start_cli():
    shell = Shell()
    try:
        shell.cmdloop()
    except KeyboardInterrupt:
        shell.do_EOF(None)