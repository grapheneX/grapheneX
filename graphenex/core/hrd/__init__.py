from graphenex.core.hrd.exec import WinExec, LinuxExec

class HardenMethod:
    """
    Class for retrieving the details of a
    module and executing the command
    """

    def __init__(self, **kwargs):
        self.linuxExec = LinuxExec()
        self.winExec = WinExec()
        self.kwargs = kwargs
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.__str__()

    def execute_command(self):
        return getattr(self, self.target_os + "Exec").run_cmd(self.command)