#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core.web import app, logger, socketio
from core.utils.helpers import check_os, get_os_info, get_modules, mod_json_file
from flask import render_template
from flask_socketio import emit
import json
import re

module_dict = get_modules()
current_namespace = list(module_dict.keys())[0]

@app.route('/')
def main():
    return render_template(
        'index.html',
        title="grapheneX [Web]",
        sys_info=get_os_info(),
        mod_count=get_mod_count(module_dict))

def get_mod_count(mod_dict):
    return sum([len(value) for key, value in mod_dict.items()])

@socketio.on('get_namespaces')
def send_namespaces(data):
    emit('get_namespaces', {'namespaces': list(module_dict.keys())})

@socketio.on('get_current_namespace')
def send_current_namespace(data):
    emit('get_current_namespace', {'current_namespace': current_namespace})

@socketio.on('send_current_namespace')
def get_current_namespace(data):
    modules = list()
    mod_dict = module_dict.get(data)
    if mod_dict == None:
        logger.warn(f"Non-existent namespace: {data}.")
    else:
        global current_namespace
        current_namespace = data
        for name, mod in mod_dict.items():
            modules.append({
                'name': name,
                'desc': mod.desc,
                'source': mod.command
            })
        logger.info(f'Sending modules of {current_namespace}.')
        emit('get_module', modules)

@socketio.on('search_module')
def search_module(data):
    result = {name: mod for name, mod in module_dict.get(
        current_namespace).items() if data["query"].lower() in name.lower()}
    payload = list()
    for name, mod in result.items():
        payload.append({
            'name': name,
            'desc': mod.desc,
            'source': mod.command
        })
    emit('search_module', {'result': payload})

@socketio.on('harden')
def hardening_exec(data):
    try:
        logger.info("Executing the hardening command of " + current_namespace + "/" + data)
        hrd = module_dict[current_namespace][data]
        out = hrd.execute_command()
        print(out)
        emit(data + "_log", {"msg": out, "state":"output"})
        success_msg = "Hardening command executed successfully."
        emit('log_message', {
            'tag': 'success',
            'content': success_msg
        })
        emit(data + "_log", {"state":"success"})
        logger.info(success_msg)
    except PermissionError:
        err_msg = "Insufficient permissions for hardening."
        if check_os():
            err_msg += " Get admin rights and rerun the grapheneX."                    
        else:
            err_msg += " Try running the grapheneX with sudo."
        emit('log_message', {
            'tag': 'warning',
            'content': err_msg,
            'duration': 2000
        })
        emit(data + "_log", {"state":"error"})
        logger.error(err_msg)
    except Exception as e:
        fail_msg = "Failed to execute hardening command."
        emit('log_message', {
            'tag': 'danger',
            'content': fail_msg,
            'duration': 2000
        })
        emit(data + "_log", {"msg": str(e), "state":"error"})
        logger.error(fail_msg + " " + str(e))

@socketio.on('add_module')
def add_module(mod):
    try:
        mod_name = mod['name']
        mod_ns = mod['ns']
        logger.info("Adding new module: '" + mod_ns + "/" + mod_name + "'")
        # Check namespace
        if not mod_ns:
            ns_error_msg = "Invalid namespace."
            logger.error(ns_error_msg)
            emit('log_message', {
            'tag': 'danger',
            'content': ns_error_msg
            })
            return
        # Check module name
        if not re.match(r'^\w+$', mod_name):
            mod_error_msg = "Invalid module name."
            logger.error(mod_error_msg)
            emit('log_message', {
            'tag': 'danger',
            'content': mod_error_msg
            })
            return
        # Get modules.json
        with open(mod_json_file, 'r') as f:
            data = json.load(f)
        # Prepare module dict
        mod_dict = {
                "name": mod_name,
                "desc": mod['desc'],
                "command": mod['cmd'],
                "require_superuser": str(mod['su']).capitalize(),
                "target_os": "win" if check_os() else "linux"
                }
        # Append to json data
        try:
            data[mod_ns].append(mod_dict)
        except:
            data.update({mod_ns: [mod_dict]})
        # Update the modules.json
        with open(mod_json_file, 'w') as f:
            json.dump(data, f, indent=4)
        success_msg = "Module added successfully."
        emit('log_message', {
            'tag': 'success',
            'content': success_msg
        })
        logger.info(success_msg)
        global module_dict
        module_dict = get_modules()
        # Success event with module count
        emit('new_module_added', get_mod_count(module_dict))
    except Exception as e:
        exception_msg = "Error occurred while adding new module. " + str(e)
        emit('log_message', {
            'tag': 'warning',
            'content': exception_msg
        })
        logger.warn(exception_msg)
