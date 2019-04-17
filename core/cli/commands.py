from core.utils.logcl import GraphenexLogger
from core.cli.help import Help
from core.utils.helpers import check_os
import os

logger = GraphenexLogger(__name__)


class ShellCommands(Help):
    def do_switch(self, arg):
        """Change module"""

        # TODO: Check control
        self.harden_str = arg

    def do_exit(self, arg):
        "Exit interactive shell"

        logger.info('Exit shell')
        print("Bye")
        return True

    def do_clear(self, arg):
        """Clear terminal"""

        os.system("cls" if check_os else "clear")

    def default(self, line):
        print("Command not found!")
