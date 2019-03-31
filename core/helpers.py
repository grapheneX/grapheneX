#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import sys
from core.logcl import GraphenexLogger

def print_header():
    # Import colorama and termcolor
    def import_colorlibs():
        try:
            global init, colored
            from colorama import init
            from termcolor import colored
            # use colorama to make termcolor work on Windows
            init()
        except:
            print("[colorama/termcolor] module not found.\n"+
            "Install requirements.txt with pip.")
            sys.exit()
    import_colorlibs()

    project_desc = """                          
           `:sdydmy/.           
        .+hNNNNNhyNNNdo:        """+colored('| grapheneX |', 'white', attrs=['bold'])+"""
     :sdNNNNNNNNNmsmNNNdys/`    Automated System Hardening Framework
     dNNNNNNNNNNNNNydmydNNN-    Created for Linux & Windows.
     dNNNNNNNNNNNNNmohNNNNN-    https://github.com/grapheneX
     dNNNNNNNNNNNmyhNNNNNNN-    Copyright (C) 2019
     dNNNNNNNNNNyhNNNNNNNNN-        
     -odNNNNNNNNmhhhhhhhhs/     
        ./ymNNNNNNNNNho-        
            :odNNmy/`                     
        """
    print(project_desc)
    GraphenexLogger("graphenex.main").info("grapheneX started.")

def check_os():
    return 1 if __import__('os').name == 'nt' else 0