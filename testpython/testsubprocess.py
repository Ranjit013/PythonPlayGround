import os
import subprocess
from pathlib import WindowsPath


def checksubProcess():
    command = 'ls -ltr'
    # output = subprocess.check_output(['‪C:\\Program Files\\Git\\git-bash.exe','-c', command])
    cmd = "find . -maxdepth 1 -type f  -name '*Resume*' | awk '{print $0}'"
    dirForShell = WindowsPath(r'C:\Users\Ranjit\Downloads')
    output = subprocess.run(['C:\Program Files\Git\\bin\\bash.exe', '-c', cmd], capture_output=True, cwd=dirForShell)
    print(output.stdout.decode())
    print(os.listdir(dirForShell))


def checkGitProcess():
    print(os.getcwd())
    command = 'git --version'
    output = subprocess.run(['C:\Program Files\Git\\bin\\bash.exe', '-c', command], capture_output=True)

    print(output.stdout.decode())


if __name__ == '__main__':
    checkGitProcess()
