import sys

from graphenex.core.utils.helpers import parse_cli_args, print_header, create_env_file
from graphenex.core.utils.logcl import GraphenexLogger
from graphenex.core.cli.shell import start_cli
from graphenex.core.web import run_server
from graphenex import __version__

logger = GraphenexLogger('Graphenex')


def main():
    args = parse_cli_args()
    if args['version']:
        print(f"grapheneX v{__version__}")
        sys.exit(0)

    create_env_file(args["flask_secret_key"])

    print_header()
    if args['web']:
        run_server(args)
    else:
        if args['open']:
            logger.warn("[--open] argument is unnecessary. " +
                        "Use with [-w] or [--web].")
        start_cli()


if __name__ == "__main__":
    main()
