import os
import sys
import json
import ctypes
import socket
import pathlib
import argparse
from colorama import init, Fore, Style
from dotenv import load_dotenv, set_key

from graphenex.core.hrd import HardenMethod
from graphenex.core.utils.logcl import GraphenexLogger


logger = GraphenexLogger(__name__)
project_dir = pathlib.Path(__file__).absolute().parent.parent.parent
mod_json_file = project_dir / "modules.json"
env_file = project_dir.parent / ".env"


def parse_cli_args():
    """
    Command-line argument parser
    Returns parsed args as dict
    """

    parser = argparse.ArgumentParser(
        description='grapheneX | Automated System Hardening Framework')
    parser.add_argument('-v',
                        '--version',
                        action="store_true",
                        help="show version information")
    parser.add_argument('-w',
                        '--web',
                        action="store_true",
                        help='start the grapheneX web server')
    parser.add_argument('host_port', metavar='host:port', type=str, nargs='?',
                        default='localhost:8080',
                        help="host and port to run the web interface")
    parser.add_argument('--open', action="store_true",
                        help="open browser on web server start")
    parser.add_argument("--flask-secret-key",
                        default=None,
                        help="Secret key to keep the client-side sessions secure.")
    args = vars(parser.parse_args())
    return args


def print_header():
    """
    Shows project logo in ASCII format,
    project description and repository
    Checks dependencies for colored output
    """
    init()
    project_desc = Style.BRIGHT + Fore.WHITE + """
                 +ho:`
           `:ohh. /dddy/.
        ./ydddddd/ -hddddho:          | grapheneX |
    `:ohdddddddddds``sddddds- :.      """+Style.NORMAL+"~ Automated System Hardening Framework"+Style.BRIGHT+"""
    +ddddddddddddddh. /dds- /hdd      """+Style.NORMAL+"+ Created for Linux & Windows."+Style.BRIGHT+"""
    +dddddddddddddddd/ .. /hdddd      """+Style.NORMAL+"> https://github.com/grapheneX"+Style.BRIGHT+"""
    +ddddddddddddddddo``/hdddddd      """+Style.NORMAL+"- Copyright (C) 2019-2024"+Style.BRIGHT+"""
    +ddddddddddddddo.`+ddddddddd
    `-/+oyhddddd+``+dddddddddddd
    :o+/-.` `-` .syddddddddddddd
    +dddddddyso+:-. `.-/+oyhdddd
     -+yddddddddddddhyso/:-` `-`
        `/sddddddddddddddy+-
            -+hddddddds:`
               `/sy+-
    """+Style.NORMAL
    print(project_desc)
    logger.info("grapheneX started.")
    check_privileges()


def check_os():
    """
    Returns operating system information.
    [1] -> Windows
    [0] -> Linux (else)
    """
    return 1 if os.name == 'nt' else 0


def check_privileges():
    """Checks privileges and warns if they aren't sufficient"""

    def is_root():
        """Returns if the app is run with sudo"""
        return os.geteuid() == 0

    def is_admin():
        """Returns if the app is run with administrative access"""
        try:
            result = ctypes.windll.shell32.IsUserAnAdmin()
            return result
        except Exception:
            return False

    if check_os():
        if not is_admin():
            logger.warn("Some functions won't work without admin rights, " +
                        "try running graphenex with admin access.")
    else:
        if not is_root():
            logger.warn("Some functions won't work without root access, " +
                        "try running grapheneX with sudo.")


def get_modules():
    """Get hardening modules & namespaces in a dictionary"""

    current_os = "win" if check_os() else "linux"
    json_data = get_mod_json()
    return_dict = dict()
    available_modules = list()
    for namespace, modlist in json_data.items():
        if namespace == "presets":
            continue
        for module in modlist:
            module['namespace'] = namespace
            if module['target_os'] == current_os:
                return_dict[module['namespace']] = dict()
                available_modules.append(module)

        for module in available_modules:
            return_dict[module['namespace']
                        ][module['name']] = HardenMethod(**module)
    return return_dict


def get_forbidden_namespaces(os='win' if check_os() else 'linux'):
    """Returns the restricted namespaces depending on the operating system"""

    json_data = get_mod_json()
    namespaces = list()
    for namespace, modlist in json_data.items():
        if os not in [module['target_os'] for module in modlist]:
            namespaces.append(namespace)
    namespaces.append("presets")
    return namespaces


def get_presets(os='win' if check_os() else 'linux'):
    """Parse and return the presets in the 'modules' file"""

    try:
        presets = list()
        for preset in get_mod_json()['presets']:
            if preset['target_os'] == os:
                presets.append(preset)
        return presets
    except KeyError:
        return None


def get_mod_json():
    """Read the modules from file"""

    try:
        with open(mod_json_file, 'r') as json_file:
            json_data = json.load(json_file)
        return json_data
    except FileNotFoundError:
        logger.error(f"{mod_json_file} not found! Exiting grapheneX.")
        sys.exit(1)


def is_valid_port(port):
    """Verify the port number"""

    return 1 <= port <= 65535


def is_valid_address(address):
    """Verify the IP address"""

    try:
        socket.getaddrinfo(address, None)
        return True
    except socket.gaierror:
        return False


def create_env_file(cli_secret_key):
    """Generate .env file with secret key"""

    env_file_exists = env_file.is_file()
    if not env_file_exists:
        env_file.touch()
        logger.info("`.env` config file created")

    load_dotenv(env_file)
    flask_secret_key = os.getenv("FLASK_SECRET_KEY")

    if cli_secret_key or not flask_secret_key:
        set_key(env_file, "FLASK_SECRET_KEY", cli_secret_key or os.urandom(32).hex())


def get_flask_secret_key():
    """Load secret key from .env file"""

    load_dotenv(env_file)
    flask_secret_key = os.getenv("FLASK_SECRET_KEY")

    return flask_secret_key
