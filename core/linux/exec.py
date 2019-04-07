#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import shlex
import subprocess

def run_cmd(cmd, **kwargs):
    """
    (LINUX) Executes command and returns it's output in UTF-8 format.
    Supports passing `kwargs`.
    """
    result = subprocess.run(shlex.split(cmd), stdout=subprocess.PIPE, **kwargs)
    return result.stdout.decode('utf-8')
