#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import shlex
import subprocess


def run_cmd(cmd, **kwargs):
    """
    (LINUX) Executes command and returns it's output in UTF-8 format.
    Supports passing `kwargs`.
    """
    args = shlex.split(cmd)
    out = subprocess.PIPE
    if args[-2] == '>' or args[-2] == '>>':
        out = open(args[-1], 'w' if args[-2] == '>' else 'a')
        args = args[:-2]
    result = subprocess.run(args, stdout=out, **kwargs)
    try:
        return result.stdout.decode('utf-8')
    except AttributeError:
        return 'stdout was redirected to a file'