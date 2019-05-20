#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

import inspect
from core.web import app, socketio
from core.utils.helpers import get_os_info, get_modules
from core.utils.logcl import GraphenexLogger
from flask import render_template
from flask_socketio import emit

logger = GraphenexLogger(__name__)

@app.route('/')
def main():
    modules = {}
    mod_desc = {}
    for i in get_modules().values():
        for k, v in i.items():
            modules[k] = inspect.getdoc(v().command)
            mod_desc[k] = inspect.getsource(v().command) \
                .split("\"\"\"")[-2]

    return render_template(
        'index.html', 
        title="grapheneX [Web]", 
        sys_info=get_os_info(),
        modules=modules,
        mod_desc=mod_desc)

# Example receive of emit
@socketio.on('connected')
def connected_event(msg):
    print(msg)

