#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

def cmd():
    return """echo "kernel.dmesg_restrict = 1" > /etc/sysctl.d/50-dmesg-restrict.conf"""
