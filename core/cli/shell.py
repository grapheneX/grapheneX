from cmd import Cmd


class Shell(Cmd):
    harden_str = ""  # this attribute is current harden module string
    intro = "Welcome Graphenex interactive shell. Type help or ? to list commands."
    prompt = f"[gX]> "

    def do_switch(self, arg):
        """Change module"""

        # TODO: Check control
        self.harden_str = arg

    def default(self, line):
        print("Command not found !")

    @property
    def prompt(self):
        return f"[gX{'' if self.harden_str == '' else ':' + self.harden_str}]> "
