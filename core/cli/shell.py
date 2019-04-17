from cmd import Cmd
from core.cli.help import Help
from core.cli.override import Override


class Shell(ShellCommands, Cmd):
    harden_str = ""  # this attribute is current harden module string
    intro = "Welcome Graphenex interactive shell. Type help or ? to list commands."
    prompt = f"[gX]> "
    doc_header = "grapheneX commands (type help <command>):"

    @property
    def prompt(self):
        return f"[gX{'' if self.harden_str == '' else ':' + self.harden_str}]> "