#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core.linux.exec import run_cmd
from core.hrd import HardenMethod

class Logs_Restrict_Access(HardenMethod):
    def command(self):
        """Restricting access to kernel logs."""

        return run_cmd("""echo "kernel.dmesg_restrict = 1" > /etc/sysctl.d/50-dmesg-restrict.conf""")

class Pointers_Restrict_Access(HardenMethod):
    def command(self):
        """Restricting access to kernel pointers."""

        return run_cmd("""echo "kernel.kptr_restrict = 1" > /etc/sysctl.d/50-kptr-restrict.conf""")
