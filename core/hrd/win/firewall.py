#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core.win.exec import run_cmd

class Disable_File_Sharing:
    def command(self):
        """Disable File and Printer Sharing."""

        return run_cmd("""netsh advfirewall firewall set rule group="File and Printer Sharing" new enable=No""")

class Disable_RDP:
    def command(self):
        """Disable Remote Desktop Protocol."""

        return run_cmd("""reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" """ + \
        """/v fDenyTSConnections /t REG_DWORD /d 1 /f""")
