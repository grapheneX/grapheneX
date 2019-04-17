from terminaltables import AsciiTable


class Help:
    """
    Help class. We must write all help commands to this class
    """

    def do_help(self, arg):
        'List available commands with "help" or detailed help with "help cmd".'
        if arg:
            try:
                func = getattr(self, f"do_{arg}")
                # Check help method for command
                try:
                    help_func = getattr(self, f"help_{arg}")
                    # Run help function
                    help_func()
                    return
                except AttributeError:  # Help method not written, use docsting
                    doc = func.__doc__ if func.__doc__ else "No description"
                    print(
                        f"\n{func.__name__[3:]} description:\n{30*'='}\n{doc}\n")

            except AttributeError:
                print('Command not found!')

        else:   # Create table all commands
            table_data = [
                ['Command', 'Description']
            ]
            for name in self.get_names():   # All class methods and attr
                if name[:3] == "do_":   # do_* handle function
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
