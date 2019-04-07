#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from winreg import *

def change_or_create_reg(valuepath, valuename, subvalue):
    """
	Changes / creates registry values using given parameters.

    valuepath: Regedit Path
    valuename: Regedit Value Name
    subvalue: Regedit Sub Value Name
    """
	key = None
    try:
        key = OpenKey(HKEY_CURRENT_USER, valuepath, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER, valuepath)
    SetValueEx(key, valuename, 0, REG_SZ, subvalue)
    CloseKey(key)       
 
def delete_reg(valuepath,valuename):
    """
	Removes value from registry.

    valuepath: Regedit Path
    valuename: Regedit Value Name
    """
    hkey = OpenKey(HKEY_CURRENT_USER, valuepath, 0, KEY_SET_VALUE)
    try:
        key = DeleteValue(hkey,valuename)
        CloseKey(hkey)
    except: pass