#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from graphenex.core.utils.logcl import GraphenexLogger

from terminaltables import AsciiTable

logger = GraphenexLogger(__name__)

class Help:
    """
    Help class that will contain help methods for spesific commands
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
                    print(f"\n\tSyntax: {func.__name__[3:]}\n\t{doc}\n")
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
            print(AsciiTable(help_table).table)

    def message(self, syntax, content):
        """Print the commands help message with its syntax"""

        print(f"\n\tSyntax: {syntax}\n\t{content}\n")

    def help_switch(self):
        self.message(syntax="switch [module]",
            content="Switch between modules")

    def help_search(self):
        self.message(syntax="search [query]",
            content="Search for module or namespace")

    def help_use(self):
        self.message(syntax="use [module]",
            content="Use hardening module")

    def help_web(self):
        self.message(syntax="web [host:port]",
            content="Start the web server")

    def help_preset(self):
        self.message(syntax="preset [preset]",
            content="Execute the hardening module preset")
