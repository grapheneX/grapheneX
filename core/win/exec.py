#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import shlex
import subprocess


def run_cmd(cmd, shell=True):
    """
    (WINDOWS) Executes command and returns it's output in UTF-8 format.
    """
    result = subprocess.run(shlex.split(
        cmd), stdout=subprocess.PIPE, shell=shell)
    return result.stdout.decode('utf-8', 'replace')
