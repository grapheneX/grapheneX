#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import sys
from core.utils.logcl import GraphenexLogger

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
    project_desc = Style.BRIGHT + Fore.WHITE + """             
                 +ho:`                
           `:ohh. /dddy/.             
        ./ydddddd/ -hddddho:          | grapheneX |
    `:ohdddddddddds``sddddds- :.      """+Style.NORMAL+"~ Automated System Hardening Framework"+Style.BRIGHT+"""
    +ddddddddddddddh. /dds- /hdd      """+Style.NORMAL+"+ Created for Linux & Windows."+Style.BRIGHT+"""
    +dddddddddddddddd/ .. /hdddd      """+Style.NORMAL+"> https://github.com/grapheneX"+Style.BRIGHT+"""
    +ddddddddddddddddo``/hdddddd      """+Style.NORMAL+"- Copyright (C) 2019"+Style.BRIGHT+"""
    +ddddddddddddddo.`+ddddddddd       
    +ddddddddddddo``+ddddddddddd      
    `-/+oyhdddd+``+ddddddddddddd      
    :o+/-.` `-` .syddddddddddddd      
    +dddddddyso+:-. `.-/+oyhdddd      
     -+yddddddddddddhyso/:-` `-`      
        `/sddddddddddddddy+-          
            -+hddddddds:`             
               `/sy+-
    """
    print(project_desc)
    GraphenexLogger("graphenex.main").info("grapheneX started.")

def check_os():
    return 1 if __import__('os').name == 'nt' else 0