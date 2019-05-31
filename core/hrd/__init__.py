from core.linux.exec import run_cmd as linux_run
from core.win.exec import run_cmd as win_run
from core.utils.logcl import GraphenexLogger

logger = GraphenexLogger(__name__)

class HardenMethod:
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return f"<HardenMethod name: {self.name}>"

    def __repr__(self):
        return self.__str__()

    def execute_command(self):
        if self.target_os == 'win':
            return win_run(self.command)
        else:
            return linux_run(self.command)