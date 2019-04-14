from core.utils.logcl import GraphenexLogger

logger = GraphenexLogger(__name__)


class ShellCommands:
    def do_switch(self, arg):
        "Change module"
 
        # TODO: Check control
        self.harden_str = arg

    def default(self, line):
        print("Command not found!")

    def do_exit(self, arg):
        "Exit interactive shell"

        logger.info('Exit shell')
        print("Bye")
        return True
