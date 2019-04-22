#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from terminaltables import AsciiTable
from core.utils.logcl import GraphenexLogger

logger = GraphenexLogger(__name__)

class Help:
    """
    Help class that will contain help methods for every command.
    """

    def do_help(self, arg):
        'List available commands with "help" or show detailed help with "help <cmd>"'

        if arg:
            try:
                func = getattr(self, f"do_{arg}")
                if (f"help_{arg}") in dir(self):
                    getattr(self, f"help_{arg}")()
                else:  
                    doc = func.__doc__ if func.__doc__ else "No description"
                    print(f"\n{func.__name__[3:]} description:\n{30*'='}\n{doc}\n")
            except AttributeError:
                logger.error(f"Cannot find help method for \"{arg}\".")
        else:   
            # Create table for all commands
            help_table = [['Command', 'Description']]
            # In all methods and attributes
            for name in self.get_names():
                # Get do_* function
                if name[:3] == "do_" and name != "do_EOF":
                    docstr = getattr(self, name).__doc__ 
                    doc = docstr if docstr else "No description"
                    help_table.append([getattr(self, name).__name__[3:], doc])
            table = AsciiTable(help_table)
            print(table.table)

    def message(self, syntax, content):
        print(f"\n\tSyntax: {syntax}\n\t{content}\n")

    def help_switch(self):
        self.message(syntax="switch [module]",
            content="Switch between modules")

    def help_search(self):
        self.message(syntax="search [module]",
            content="Search for module or namespace")