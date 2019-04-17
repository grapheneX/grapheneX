#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

class Logs_Restrict_Access:
    def command(self):
        """Restricting access to kernel logs."""

        return """echo "kernel.dmesg_restrict = 1" > /etc/sysctl.d/50-dmesg-restrict.conf"""
        