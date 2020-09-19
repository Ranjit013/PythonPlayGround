import subprocess

bashCommand = "dir"
subprocess.Popen(["C:\Program Files\Git\git-bash.exe", "test.sh"],
                 bufsize=-1,
                 executable=None,
                 stdin=None,
                 stdout=None,
                 stderr=None,
                 preexec_fn=None,
                 close_fds=True,
                 shell=False,
                 cwd="C:/Users/Ranjit/workspace/PythonPlayGround/shellinpython/shellfiles",
                 )

if __name__ == '__main__':
    print('Hello World')
