#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

class Disable_File_Sharing:
    def command(self):
        """Disable File and Printer Sharing."""

        return """netsh advfirewall firewall set rule group="File and Printer Sharing" new enable=No"""

class Disable_RDP:
    def command(self):
        """Disable Remote Desktop Protocol."""

        return """reg add "HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server" """ + \
        """/v fDenyTSConnections /t REG_DWORD /d 1 /f"""
                