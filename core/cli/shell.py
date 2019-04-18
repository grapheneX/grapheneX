#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from cmd import Cmd
from core.cli.commands import ShellCommands

class Shell(ShellCommands, Cmd):
    # Current harden module string
    harden_str = ""
    intro = "Welcome to the grapheneX interactive shell. Type \"help\" or \"?\" to list commands."
    prompt = f"[gX]> "

    @property
    def prompt(self):
        return f"[gX{'' if self.harden_str == '' else ':' + self.harden_str}]> "