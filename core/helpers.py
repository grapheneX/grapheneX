#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import sys
from core.logcl import GraphenexLogger

def print_header():
    # Import colorama
    def import_colorama():
        try:
            global init, Fore, Style, colored
            from colorama import init, Fore, Style
            init()
        except:
            print("colorama module not found.\n"+
            "Install requirements.txt with pip.")
            sys.exit()
    import_colorama()

    project_desc = Style.BRIGHT + """                          
           `:sdydmy/.           
        .+hNNNNNhyNNNdo:        | grapheneX |
     :sdNNNNNNNNNmsmNNNdys/`    """+Style.NORMAL+"Automated System Hardening Framework"+Style.BRIGHT+"""
     dNNNNNNNNNNNNNydmydNNN-    """+Style.NORMAL+"Created for Linux & Windows."+Style.BRIGHT+"""
     dNNNNNNNNNNNNNmohNNNNN-    """+Style.NORMAL+"https://github.com/grapheneX"+Style.BRIGHT+"""
     dNNNNNNNNNNNmyhNNNNNNN-    """+Style.NORMAL+"Copyright (C) 2019"+Style.BRIGHT+"""
     dNNNNNNNNNNyhNNNNNNNNN-        
     -odNNNNNNNNmhhhhhhhhs/     
        ./ymNNNNNNNNNho-        
            :odNNmy/`                     
        """
    print(project_desc)
    GraphenexLogger("graphenex.main").info("grapheneX started.")

def check_os():
    return 1 if __import__('os').name == 'nt' else 0