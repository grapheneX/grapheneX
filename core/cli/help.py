from terminaltables import AsciiTable


class Help:
    """
    Help class that will contain help methods for every command.
    """

    def do_help(self, arg):
        'List available commands with "help" or show detailed help with "help <cmd>".'
        if arg:
            try:
                func = getattr(self, f"do_{arg}")
                # Check help method for command
                try:
                    help_func = getattr(self, f"help_{arg}")
                    # Run help function
                    help_func()
                except AttributeError:  
                    # Help method not available, use docstring instead
                    doc = func.__doc__ if func.__doc__ else "No description"
                    print(f"\n{func.__name__[3:]} description:\n{30*'='}\n{doc}\n")
            except AttributeError:
                print(f"Cannot find help method for \"{arg}\".")
        else:   
            # Create table for all commands
            table_data = [['Command', 'Description']]
            # In all methods and attr
            for name in self.get_names():
                # Get do_* function
                if name[:3] == "do_":  
                    func = getattr(self, name)
                    doc = func.__doc__
                    if not doc:
                        doc = "No description"
                    table_data.append([func.__name__[3:], doc])
            table = AsciiTable(table_data)
            print(table.table)

    def message(self, syntax, content):
        print(f"\n\tSyntax: {syntax}\n\t{content}\n")

    def help_switch(self):
        self.message(syntax="switch [module]",
                     content="Switch between modules")
