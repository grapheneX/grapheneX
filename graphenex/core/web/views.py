#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from graphenex.core.web import app, logger
from graphenex.core.utils.helpers import check_os, get_modules, mod_json_file
from graphenex.core.utils.sysinfo import SysInformation

from flask import render_template, session, request, redirect, flash, jsonify
from functools import wraps
import json
import re

module_dict = get_modules()
current_namespace = list(module_dict.keys())[0]


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = session.get('token', None)
        if token != app.config['ACCESS_TOKEN']:
            return redirect('/auth')
        else:
            return f(*args, **kwargs)
    return decorated_function

def auth_api(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('token', None) == app.config['ACCESS_TOKEN']:
            return f(*args, **kwargs)
        else:
            return jsonify({'msg': 'Not authenticated'})

    return decorated_function


@app.route('/auth', methods=["GET", "POST"])
def auth():
    if session.get('token', None) == app.config['ACCESS_TOKEN']:
        return redirect('/')

    if request.method == 'POST':
        token = request.form['token']
        if token == app.config['ACCESS_TOKEN']:
            session['token'] = token
            return redirect('/')
        else:
            flash('Token is not valid', 'error')

    return render_template('auth.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
@login_required
def front():
    return render_template('index.html')


@app.route('/api/getsysteminfo')
@auth_api
def get_system_info():
    return jsonify(SysInformation.get_all_info())


@app.route('/api/getnetwork')
@auth_api
def get_network():
    return jsonify(SysInformation.get_network_info())


@app.route('/api/getnamespaces')
@auth_api
def get_namespaces():
    return jsonify(list(module_dict.keys()))


@app.route('/api/getmodules', methods=['POST'])
@auth_api
def getmodules():
    namespace = request.json.get('namespace')
    mod_dict = module_dict.get(namespace)
    modules = list()
    for name, mod in mod_dict.items():
        modules.append({
            'name': name,
            'desc': mod.desc,
            'source': mod.command
        })
    logger.info(f'Sending modules of \"{namespace}\".')
    return jsonify(modules)


@app.route('/api/search', methods=['POST'])
@auth_api
def search():
    query = request.json.get('query')
    result = {name: mod for name, mod in module_dict.get(
        current_namespace).items() if query.lower() in name.lower()}
    payload = list()
    for name, mod in result.items():
        payload.append({
            'name': name,
            'desc': mod.desc,
            'source': mod.command
        })
    return jsonify({"result": payload})


@app.route('/api/harden', methods=['POST'])
@auth_api
def hardening_exec():
    data = request.json.get('module_name')
    """Execute the hardening module and send its output to web"""
    try:
        logger.info("Executing the hardening command of " +
                    current_namespace + "/" + data)
        hrd = module_dict[current_namespace][data]
        out = hrd.execute_command()
        print(out)
        return jsonify({"status": True, "msg": "Hardening command executed successfully.", "stdout": out})
    except PermissionError:
        err_msg = "Insufficient permissions for hardening."
        if check_os():
            err_msg += " Get admin rights and rerun the grapheneX."
        else:
            err_msg += " Try running the grapheneX with sudo."
        logger.error(err_msg)
        return jsonify({"status": False, "msg": err_msg})
    except Exception as e:
        return jsonify({"status": False, "msg": "Failed to execute hardening command."})


@app.route('/api/addmodule', methods=['POST'])
@auth_api
def add_module():
    mod = request.json.get('moduleObj')
    """Add new module to the framework"""
    try:
        mod_name = mod['name']
        mod_ns = mod['namespace']
        logger.info("Adding new module: '" + mod_ns + "/" + mod_name + "'")
        # Check namespace
        if not mod_ns:
            ns_error_msg = "Invalid namespace."
            logger.error(ns_error_msg)
            return jsonify({"status": False, "msg": ns_error_msg})
        # Check module name
        if not re.match(r'^\w+$', mod_name):
            mod_error_msg = "Invalid module name."
            logger.error(mod_error_msg)
            return jsonify({"status": False, "msg": mod_error_msg})
        # Get modules.json
        with open(mod_json_file, 'r') as f:
            data = json.load(f)
        # Prepare module dict
        mod_dict = {
            "name": mod_name,
            "desc": mod['desc'],
            "command": mod['command'],
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
        logger.info(success_msg)
        global module_dict
        module_dict = get_modules()
        
        return jsonify({"status": True, "msg": success_msg})
    except Exception as e:
        exception_msg = "Error occurred while adding new module. " + str(e)
        logger.warn(exception_msg)
        return jsonify({"status": False, "msg": exception_msg})


def get_mod_count(mod_dict):
    """Return the count of modules in the dict"""
    return sum([len(value) for key, value in mod_dict.items()])
