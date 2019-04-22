#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import sys
import os
import importlib.util
import inspect
from core.utils.logcl import GraphenexLogger

logger = GraphenexLogger(__name__)

def print_header():
    """ 
    Shows project logo in ASCII format,
    project description and repository.
    Checks dependencies for colored output.
    """
    # Import colorama
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
    """
    print(project_desc)
    logger.info("grapheneX started.")


def check_os():
    """
    Returns operating system information.
    [1] -> Windows
    [0] -> Linux (else)
    """
    return 1 if __import__('os').name == 'nt' else 0

def get_modules():
    """
    Returns hardening modules as dict
    """
    hrd_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            '..', 'hrd')
    hrd_os = 'win' if check_os() else 'linux'
    files = [os.path.join(hrd_dir, hrd_os, f) for f in os.listdir(os.path.join(hrd_dir, hrd_os)) if f.endswith('.py')]
    modules = dict()
    for path in files:
        module_name = os.path.basename(path)[:-3]
        spec = importlib.util.spec_from_file_location(module_name, path)
        hrd = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(hrd)
        modules[module_name] = {}
        for name, obj in inspect.getmembers(hrd, inspect.isclass):
            modules[module_name][name] = obj
    return modules

