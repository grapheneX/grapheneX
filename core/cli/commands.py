from core.utils.logcl import GraphenexLogger
from core.cli.help import Help

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

    def default(self, line):
        print("Command not found!")
