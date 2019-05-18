#!/usr/bin/python3.7
# -*- coding: utf-8 -*-

from core.web import app, socketio
from core.utils.helpers import get_os_info, get_modules
from core.utils.logcl import GraphenexLogger
from flask import render_template
from flask_socketio import emit

logger = GraphenexLogger(__name__)

@app.route('/')
def main():
    return render_template(
        'index.html', 
        title="grapheneX [Web]", 
        sys_info=get_os_info(),
        namespaces=get_modules())

# Example receive of emit
@socketio.on('connected')
def connected_event(msg):
    print(msg)
