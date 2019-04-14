from cmd import Cmd

from core.cli.commands import ShellCommands

class Shell(Cmd, ShellCommands):
    harden_str = ""  # this attribute is current harden module string
    intro = "Welcome Graphenex interactive shell. Type help or ? to list commands."
    prompt = f"[gX]> "

    @property
    def prompt(self):
        return f"[gX{'' if self.harden_str == '' else ':' + self.harden_str}]> "
