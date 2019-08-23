from graphenex.core.cli.shell import Shell
from graphenex.core.utils.logcl import GraphenexLogger

from flask import Flask
from flask_socketio import SocketIO
import webbrowser
import secrets

logger = GraphenexLogger(__name__)
app = Flask(__name__)
app.config['SECRET_KEY'] = '77a98d7971ec94c8aae6dd2d'
app.config['ACCESS_TOKEN'] = secrets.token_urlsafe(6)
socketio = SocketIO(app)
default_addr = ('localhost', '8080')

from graphenex.core.web.views import *

def disable_flask_logs():
    """Disable the Flask logs"""

    import logging
    log = logging.getLogger('werkzeug').setLevel(logging.ERROR)

def run_server(args=None, exit_shell=True):
    """Run the web server"""

    disable_flask_logs()
    try:
        if args:
            server_params = args['host_port'].split(':') \
                if ':' in args['host_port'] \
                else (args['host_port'], '8080')
        else:
            server_params = default_addr
        logger.info(f"Starting server: http://{server_params[0]}:{server_params[1]}")
        try:
            if args and args['open']:
                webbrowser.open(f"http://{server_params[0]}:{server_params[1]}")
        except:
            pass
        logger.info(f"Your access token: {app.config['ACCESS_TOKEN']}")
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
