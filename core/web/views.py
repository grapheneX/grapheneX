#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core.web import app, socketio
from core.utils.helpers import get_os_info, get_modules
from core.utils.logcl import GraphenexLogger
from flask import render_template
from flask_socketio import emit
import inspect

logger = GraphenexLogger(__name__)
namespaces = get_modules()

@app.route('/')
def main():
    modules = {}
    for i in get_modules().values():
        for k, v in i.items():
            modules[k] = inspect.getdoc(v().command)

    return render_template(
        'index.html', 
        title="grapheneX [Web]", 
        sys_info=get_os_info(),
        namespaces=namespaces,
        modules=modules)

# Example receive of emit
@socketio.on('connected')
def connected_event(msg):
    print(msg)

@socketio.on('namespace')
def namespace_changed(namespace):
	data = {}
	for name, module in modules[namespace].items():
		data[name] = inspect.getdoc(module.command)
	emit("modules", {'modules' : data})