#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

def check_os():
    return 1 if __import__('os').name == 'nt' else 0

def print_header():
    project_desc = """                          
           `:sdydmy/.           
        .+hNNNNNhyNNNdo:        | grapheneX |
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