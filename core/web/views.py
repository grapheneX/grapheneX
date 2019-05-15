from core.web import app, socketio
from core.utils.helpers import get_os_info
from core.utils.logcl import GraphenexLogger
from flask import render_template
from flask_socketio import emit

logger = GraphenexLogger(__name__)

@app.route('/')
def main():
    return render_template('index.html', title="grapheneX [Web]", sys_info=get_os_info())

# Don't use this method
# We will sending system information in render_template
@socketio.on('request system info')
def request_system_info(data):
    logger.info("Sending system info")
    emit("response system info", get_os_info())

@socketio.on('connected')
def connected_event(msg):
    print(msg)
