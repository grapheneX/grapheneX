#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core.utils.logcl import GraphenexLogger
from core.cli.help import Help
from core.utils.helpers import check_os

from terminaltables import AsciiTable
import inspect
import random
import os

logger = GraphenexLogger(__name__)

class ShellCommands(Help):
    def do_switch(self, arg):
        """Switch between modules or namespaces"""

        if arg:
            arg = arg.lower()
            if arg in self.modules.keys():
                logger.info(f"Switched to \"{arg}\" namespace." +
                            " Use 'list' to see available modules.")
                self.namespace = arg
                self.module = ""
            else:
                self.do_use(arg)
        else:
            logger.warn("'switch' command takes 1 argument.")

    def complete_switch(self, text, line, begidx, endidx):
        avb_namespaces = [i.lower() for i in self.modules.keys()]
        mline = line.lower().partition(' ')[2]
        offs = len(mline) - len(text)
        return [s[offs:] for s in avb_namespaces if s.startswith(mline)]

    def do_use(self, arg):
        """Use hardening module"""

        if "/" in arg and arg.split("/")[0].lower() in self.modules.keys():
            self.namespace = arg.split("/")[0].lower()
            arg = arg.split("/")[1]

        def select_module_msg(module):
            logger.info(f"\"{module}\" module selected. Use 'harden' command " +
                        "for hardening or use 'info' for more information.")
        if arg:
            module_found = False
            if self.namespace:
                for name, module in self.modules[self.namespace].items():
                    if arg.lower() == name.lower():
                        module_found = True
                        self.module = name
                        select_module_msg(self.module)
            else:
                for k, v in self.modules.items():
                    for name, module in v.items():
                        if arg.lower() == name.lower():
                            module_found = True
                            self.module = name
                            self.namespace = k
                            select_module_msg(self.module)
            if not module_found:
                logger.error(f"No module/namespace named \"{arg}\".")
        else:
            logger.warn("'use' command takes 1 argument.")

    def complete_use(self, text, line, begidx, endidx):
        avb_modules = self.modules.get(self.namespace)
        if avb_modules is None:
            avb_modules = list()
            for key, value in self.modules.items():
                for name, module in value.items():
                    avb_modules.append(f"{key}/{name}")
        mline = line.lower().partition(' ')[2]
        # If namespace selected
        if '/' in mline:
            # title() given module string for getting rid of case sensitivity
            mline = mline.split('/')[0].lower() + "/" + \
                mline.split('/')[1].title()
        offs = len(mline) - len(text)
        # Get completed text with namespace
        comp_text = [s[offs:] for s in avb_modules if s.startswith(mline)]
        # If no namespace found
        if len(comp_text) == 0:
            # Try to complete with module names
            avb_modules = list()
            for key, value in self.modules.items():
                for name, module in value.items():
                    avb_modules.append(name)
            mline = mline.title()
            comp_text = [s[offs:] for s in avb_modules if s.startswith(mline)]
        return comp_text
            
    def do_info(self, arg):
        """Information about the desired module"""
        
        if self.module:
            print(self.modules[self.namespace][self.module]().command.__doc__)
        else:
            print("Please select module.")

    def do_search(self, arg):
        """Search for modules"""

        search_table = [['Module', 'Description']]
        if arg:
            if arg in self.modules.keys():
                for name, module in self.modules[arg].items():
                    search_table.append(
                        [arg.upper() + "." + name, inspect.getdoc(module.command)])
            else:
                for k, v in self.modules.items():
                    for name, module in v.items():
                        if arg.lower() in name.lower():
                            search_table.append(
                                [k.upper() + "." + name, inspect.getdoc(module.command)])
            if len(search_table) > 1:
                print(AsciiTable(search_table).table)
            else:
                logger.error(f"Nothing found for \"{arg}\".")
        else:
            self.do_list(None)

    def do_list(self, arg):
        """List available hardening modules"""

        modules_table = [['Module', 'Description']]
        if self.namespace:
            for name, module in self.modules[self.namespace].items():
                modules_table.append([name, inspect.getdoc(module.command)])
        else:
            for k, v in self.modules.items():
                for name, module in v.items():
                    modules_table.append(
                        [k.upper() + "." + name, inspect.getdoc(module.command)])
        print(AsciiTable(modules_table).table)

    def do_back(self, arg):
        """Go back if namespace (hardening method) selected or switched"""

        if(self.module):
            self.module = ""
        else:
            self.namespace = ""

    def do_harden(self, arg):
        """Execute the hardening method"""

        if not (self.module and self.namespace):
            logger.error('Select a module/namespace.')
        else:
            hrd = self.modules[self.namespace][self.module]()
            out = hrd.command()
            print(out)

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
        print()
        self.do_exit(arg)

    def do_clear(self, arg):
        """Clear terminal"""

        os.system("cls" if check_os() else "clear")

    def default(self, line):
        logger.error("Command not found.")
