#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core.web import app, logger, socketio
from core.utils.helpers import get_os_info, get_modules
from core.utils.logcl import GraphenexLogger

from flask import render_template
from flask_socketio import emit

import inspect

module_dict = get_modules()
current_namespace = list(module_dict.keys())[0]


@app.route('/')
def main():
    return render_template(
        'index.html',
        title="grapheneX [Web]",
        sys_info=get_os_info())

# Namespace stuff
@socketio.on('get_namespaces')
def send_namespaces(data):
    logger.info('Sending namespace list...')
    emit('get_namespaces', {'namespaces': list(module_dict.keys())})

    # This is test code
    # emit('get_namespaces', {'namespaces': ['firewall', 'network', 'general']})


@socketio.on('get_current_namespace')
def send_current_namespace(data):
    logger.info('Sending current namespace...')
    emit('get_current_namespace', {'current_namespace': current_namespace})


@socketio.on('send_current_namespace')
def get_current_namespace(data):
    logger.info(f'Current namespace changed: {data}')

    logger.info(f'Sending modules by {data}')
    modules = list()
    mod_dict = module_dict.get(data)
    if mod_dict == None:
        logger.warn(f"non-existent namespace: {data}")
        return 0

    current_namespace = data
    for name, mod in mod_dict.items():
        modules.append({
            'name': name,
            'desc': inspect.getdoc(mod().command),
            'source': inspect.getsource(mod().command).split("\"\"\"")[-2]
        })

    emit('get_module', modules)

# Search module
@socketio.on('search_module')
def search_module(data):
    result = {name: mod for name, mod in module_dict.get(
        current_namespace).items() if data["query"] in name}

    payload = list()
    for name, mod in result.items():
        payload.append({
            'name': name,
            'desc': inspect.getdoc(mod().command),
            'source': inspect.getsource(mod().command).split("\"\"\"")[-2]
        })
        
    emit('search_module', {'result': payload})
