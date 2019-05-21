#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core.web import app, socketio
from core.utils.helpers import get_os_info, get_modules
from core.utils.logcl import GraphenexLogger

from flask import render_template
from flask_socketio import emit
import inspect


logger = GraphenexLogger(__name__)

module_dict = get_modules()
current_namespace = list(module_dict.keys())[0]


@app.route('/')
def main():
    # for i in get_modules().values():
    #    for k, v in i.items():
    #        modules[k] = inspect.getdoc(v().command)
    #        mod_desc[k] = inspect.getsource(v().command).split("\"\"\"")[-2]
    return render_template(
        'index.html',
        title="grapheneX [Web]",
        sys_info=get_os_info())

# Example receive of emit
@socketio.on('connected')
def connected_event(msg):
    print(msg)


@socketio.on('get_namespaces')
def send_namespaces(data):
    # emit('get_namespaces', {'namespaces': list(module_dict.keys())})  --> this is original code

    # This is test code
    emit('get_namespaces', {'namespaces': ['firewall', 'network', 'general']})

@socketio.on('get_current_namespace')
def send_current_namespace(data):
    emit('get_current_namespace', {'current_namespace': current_namespace})