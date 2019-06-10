#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import sys
import os
import importlib.util
import inspect
import ctypes
import platform
import pathlib
import json

from core.hrd import HardenMethod
from core.utils.logcl import GraphenexLogger

logger = GraphenexLogger(__name__)

PROJECT_DIR = pathlib.Path.cwd()
mod_json_file = PROJECT_DIR / 'modules.json'


def print_header():
    """
    Shows project logo in ASCII format,
    project description and repository.
    Checks dependencies for colored output.
    """
    def import_colorama():
        try:
            global init, Fore, Style, colored
            from colorama import init, Fore, Style
            init()
        except:
            print("colorama module not found.\n" +
                  "Install requirements.txt with pip.")
            sys.exit()
    import_colorama()
    project_desc = Style.BRIGHT + Fore.WHITE + """
                 +ho:`
           `:ohh. /dddy/.
        ./ydddddd/ -hddddho:          | grapheneX |
    `:ohdddddddddds``sddddds- :.      """+Style.NORMAL+"~ Automated System Hardening Framework"+Style.BRIGHT+"""
    +ddddddddddddddh. /dds- /hdd      """+Style.NORMAL+"+ Created for Linux & Windows."+Style.BRIGHT+"""
    +dddddddddddddddd/ .. /hdddd      """+Style.NORMAL+"> https://github.com/grapheneX"+Style.BRIGHT+"""
    +ddddddddddddddddo``/hdddddd      """+Style.NORMAL+"- Copyright (C) 2019"+Style.BRIGHT+"""
    +ddddddddddddddo.`+ddddddddd
    `-/+oyhddddd+``+dddddddddddd
    :o+/-.` `-` .syddddddddddddd
    +dddddddyso+:-. `.-/+oyhdddd
     -+yddddddddddddhyso/:-` `-`
        `/sddddddddddddddy+-
            -+hddddddds:`
               `/sy+-
    """+Style.NORMAL
    print(project_desc)
    logger.info("grapheneX started.")
    check_privileges()

def check_os():
    """
    Returns operating system information.
    [1] -> Windows
    [0] -> Linux (else)
    """
    return 1 if __import__('os').name == 'nt' else 0

def check_privileges():
    """Checks privileges and warns if they aren't sufficient"""
    if check_os():
        if not is_admin():
            logger.warn("Some functions won't work without admin rights, " +
                        "try running the graphenex with admin access.")
    else:
        if not is_root():
            logger.warn("Some functions won't work without root access, " +
                        "try running the grapheneX with sudo.")

def is_root():
    """Returns if the app is run with sudo"""
    return os.geteuid() == 0

def is_admin():
    """Returns if the app is run with administrative access"""
    try:
        result = ctypes.windll.shell32.IsUserAnAdmin()
        return result
    except:
        return False


def get_os_info():
    uname = platform.uname()
    return {
        'system': f"{uname.system} | {uname.version}",
        'processor': f"{uname.processor} - ({uname.machine})"
    }

def get_modules(path=PROJECT_DIR):
    current_os="win" if check_os() else "linux"
    with open(path / 'modules.json', 'r') as json_file:
        json_data = json.load(json_file)
    return_dict = dict()
    available_modules = list()
    for namespace, modlist in json_data.items():
        for module in modlist:
            module['namespace'] =  namespace
            if module['target_os'] == current_os:
                return_dict[module['namespace']] = dict()
                available_modules.append(module)

        for module in available_modules:
            return_dict[module['namespace']][module['name']] = HardenMethod(**module)
    return return_dict

def get_forbidden_namespaces(path=PROJECT_DIR,os='win' if check_os() else 'linux'):
    with open(path / 'modules.json', 'r') as json_file:
        json_data = json.load(json_file)
    namespaces = list()
    for namespace, modlist in json_data.items():
        if os not in [module['target_os'] for module in modlist]:
            namespaces.append(namespace)
    return namespaces
