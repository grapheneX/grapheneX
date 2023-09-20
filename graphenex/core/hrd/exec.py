import os
import shlex
import subprocess
from abc import ABC, abstractmethod


class OsExec(ABC):
    @abstractmethod
    def run_cmd(self, cmd):
        pass


class LinuxExec(OsExec):
    def run_cmd(self, cmd, shell=True, **kwargs):
        """
        Executes the Linux command and returns it's output in UTF-8 format.
        Supports passing `kwargs`.
        """

        cmd = cmd.replace("$USER", os.environ["USER"])
        result = subprocess.run(cmd, stdout=subprocess.PIPE, shell=shell, **kwargs)
        if result.returncode != 0:
            raise PermissionError

        try:
            return result.stdout.decode('utf-8')
        except AttributeError:
            return 'stdout was redirected to a file'


class WinExec(OsExec):
    def run_cmd(self, cmd, shell=True):
        """
        Executes the Windows command and returns it's output in UTF-8 format.
        """
        
        result = subprocess.run(shlex.split(
            cmd), stdout=subprocess.PIPE, shell=shell)
        return result.stdout.decode('utf-8', 'replace')
