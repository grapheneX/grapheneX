#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from winreg import *
from core.utils.logcl import GraphenexLogger

def change_or_create_reg(valuepath, valuename, subvalue):
    """
	Changes / creates registry values using given parameters.

    valuepath: Regedit Path
    valuename: Regedit Value Name
    subvalue: Regedit Sub Value Name
    """
	log = GraphenexLogger("graphenex.reg")
	log.info("Changing/creating registry value: " + valuename)
	key = None
    try:
        key = OpenKey(HKEY_CURRENT_USER, valuepath, 0, KEY_ALL_ACCESS)
    except:
        key = CreateKey(HKEY_CURRENT_USER, valuepath)
    SetValueEx(key, valuename, 0, REG_SZ, subvalue)
    CloseKey(key)
	log.info("Registry updated.")
 
def delete_reg(valuepath, valuename):
    """
	Removes value from registry.

    valuepath: Regedit Path
    valuename: Regedit Value Name
    """
	log = GraphenexLogger("graphenex.reg")
	log.info("Deleting registry value: " + valuename)
    hkey = OpenKey(HKEY_CURRENT_USER, valuepath, 0, KEY_SET_VALUE)
    try:
        key = DeleteValue(hkey,valuename)
        CloseKey(hkey)
		log.info("Registry updated.")
    except:
		log.info("Unable to delete registry value: " + valuename)