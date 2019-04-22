#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core.utils.logcl import GraphenexLogger
from core.cli.help import Help
from core.utils.helpers import check_os, get_modules
from terminaltables import AsciiTable
import inspect
import random
import os

logger = GraphenexLogger(__name__)

class ShellCommands(Help):
    def do_switch(self, arg):
        """Change module"""

        # TODO: Check control
        self.harden_str = arg

    def do_exit(self, arg):
        "Exit interactive shell"

        exit_msgs = [
            "Bye!",
            "Hope to see you soon!",
            "Take care!",
            "I am not going to miss you!",
            "Gonna miss you!",
            "Thank God, you're leaving. What a relief!",
            "Fare thee well!",
            "Farewell, boss.", 
            "Daha karpuz kesecektik.",
            "Bon voyage!",
            "Regards.",
            "Exiting..."]
        logger.info(random.choice(exit_msgs))
        return True

    def do_EOF(self, arg):
        self.do_exit(arg)
        return True

    def do_clear(self, arg):
        """Clear terminal"""

        os.system("cls" if check_os() else "clear")

    def do_search(self, arg):
        """Search for modules"""

        modules = get_modules()
        search_table = [['Module', 'Description']]
        if arg:
            if arg in modules.keys():
                for name, module in modules[arg].items():
                    search_table.append([arg.upper() + "." + name, inspect.getdoc(module.command)])
            else:
                for k, v in modules.items():
                    for name, module in v.items():
                        if arg.lower() in name.lower():
                            search_table.append([k.upper() + "." + name, inspect.getdoc(module.command)])        
            if len(search_table) > 1:
                print(AsciiTable(search_table).table)
            else:
                logger.error(f"Nothing found for \"{arg}\".")
        else:
            self.do_ls(None)
        
    def do_ls(self, arg):
        """List hardening modules"""
        
        modules = get_modules()
        modules_table = [['Module', 'Description']]
        for k, v in modules.items():
                for name, module in v.items():
                    modules_table.append([k.upper() + "." + name, inspect.getdoc(module.command)])
        print(AsciiTable(modules_table).table)

    def default(self, line):
        logger.error("Command not found.")