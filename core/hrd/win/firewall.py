#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

class Disable_File_Sharing:
    def command(self):
        """Disable File and Printer Sharing."""

        return """netsh advfirewall firewall set rule group="File and Printer Sharing" new enable=No"""
        