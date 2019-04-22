#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core.utils.logcl import GraphenexLogger
from core.cli.help import Help
from core.utils.helpers import check_os
from pprint import pprint
import importlib.util
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
        hrd_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                '..', 'hrd')

        hrd_os = 'win' if check_os() else 'linux'
        files = [os.path.join(hrd_dir, hrd_os, f) for f in os.listdir(os.path.join(hrd_dir, hrd_os)) if f.endswith('.py')]

        modules = dict()
        for path in files:
            module_name = os.path.basename(path)[:-3]
            spec = importlib.util.spec_from_file_location(module_name, path)
            hrd = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(hrd)
            modules[module_name] = {}
            for name, obj in inspect.getmembers(hrd, inspect.isclass):
                modules[module_name][name] = obj

        if not arg:
            for k, v in modules.items():
                print(k)
                for name, module in v.items():
                    print(' +--', name, '-->', inspect.getdoc(module.command))
        else:
            if arg in modules.keys():
                print(arg)
                for name, module in modules[arg].items():
                    print(' +--', name, '-->', inspect.getdoc(module.command))
            else:
                for k, v in modules.items():
                    for name, module in v.items():
                        if arg.lower() in name.lower():
                            print(name, '-->', inspect.getdoc(module.command))


    def default(self, line):
        logger.error("Command not found.")
