from core.utils.logcl import GraphenexLogger
from core.cli.shell import Shell
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

logger = GraphenexLogger(__name__)
app = Flask(__name__)
socketio = SocketIO(app)
default_addr = ('0.0.0.0', '8080')

@app.route('/')
def main():
    return render_template('index.html', title="grapheneX [Web]")

def run_server(args=None):
    try:
        if args:
            server_params = args['host_port'].split(':') \
                if ':' in args['host_port'] \
                else (args['host_port'], '8080')
        else:
            server_params = default_addr
        logger.info("Starting server: [http://" + server_params[0] + ":" + server_params[1] + "]")
        socketio.run(app, host=server_params[0], port=int(server_params[1]), debug=False)
    except (PermissionError, ValueError):
        logger.error('Invalid host & port address. Restarting with default host and port.')
        run_server()
    except KeyboardInterrupt:
        socketio.stop()
        Shell().do_exit(None)
    except Exception as e:
        logger.error('An error occurred: ' + str(e))
        
@socketio.on('my_event')
def handle_my_event(json):
    emit('Test Response', json)
