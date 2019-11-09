from graphenex.core.cli.shell import Shell
from graphenex.core.utils.logcl import GraphenexLogger
from graphenex.core.utils.helpers import project_dir

from flask import Flask
import jinja2
import webbrowser
import secrets


logger = GraphenexLogger(__name__)

static_folder = project_dir / 'core' / 'web' / 'frontend' / 'static'
app = Flask(__name__, static_folder=static_folder)
app.config['SECRET_KEY'] = '77a98d7971ec94c8aae6dd2d'
app.config['ACCESS_TOKEN'] = secrets.token_urlsafe(6)


default_addr = ('localhost', '8080')

# Added template folder for react
template_dir = project_dir / 'core' / 'web' / 'frontend' / 'public'
template_loader = jinja2.ChoiceLoader([
    app.jinja_loader,
    jinja2.FileSystemLoader(str(template_dir))
])

app.jinja_loader = template_loader

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
        logger.info(
            f"Starting server: http://{server_params[0]}:{server_params[1]}")
        try:
            if args and args['open']:
                webbrowser.open(
                    f"http://{server_params[0]}:{server_params[1]}")
        except:
            pass
        
        logger.info(f"Your access token: {app.config['ACCESS_TOKEN']}")
        app.run(host=server_params[0], port=int(
            server_params[1]), debug=False)
    except (PermissionError, ValueError):
        logger.error(
            'Invalid host & port address. Restarting with default host and port.')
        run_server()
    except KeyboardInterrupt:
        if exit_shell:
            Shell().do_exit(None)
    except Exception as e:
        logger.error('An error occurred: ' + str(e))
