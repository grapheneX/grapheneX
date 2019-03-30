import shlex
import subprocess

def run_cmd(cmd, shell=False):
    result = subprocess.run(shlex.split(cmd), stdout=subprocess.PIPE, shell=shell)
    return result.stdout.decode('utf-8')
