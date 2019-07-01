from flask import Flask
from flask_socketio import SocketIO
from core.cli.shell import Shell
from core.utils.logcl import GraphenexLogger

import webbrowser

logger = GraphenexLogger(__name__)
app = Flask(__name__)
app.config['SECRET_KEY'] = '77a98d7971ec94c8aae6dd2d'
socketio = SocketIO(app)
default_addr = ('0.0.0.0', '8080')

from core.web.views import *

def disable_flask_logs():
    import logging
    log = logging.getLogger('werkzeug').setLevel(logging.ERROR)

def run_server(args=None, exit_shell=True):
    disable_flask_logs()
    try:
        if args:
            server_params = args['host_port'].split(':') \
                if ':' in args['host_port'] \
                else (args['host_port'], '8080')
        else:
            server_params = default_addr
        starting_msg = "Starting server: [http://" + server_params[0] + ":" + server_params[1] + "]"
        if server_params[0] == "0.0.0.0": starting_msg += " (localhost:" + server_params[1] + ")"
        logger.info(starting_msg)
        if args['open']:
            webbrowser.open(f"http://{'localhost' if server_params[0] == '0.0.0.0' else server_params[0]}:{server_params[1]}")
        socketio.run(app, host=server_params[0], port=int(server_params[1]), debug=False)
    except (PermissionError, ValueError):
        logger.error('Invalid host & port address. Restarting with default host and port.')
        run_server()
    except KeyboardInterrupt:
        socketio.stop()
        if exit_shell:
            Shell().do_exit(None)
    except Exception as e:
        logger.error('An error occurred: ' + str(e))