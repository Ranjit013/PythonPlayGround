import argparse
import sys


# print(sys.argv)
#
# path = WindowsPath(r'C:\Users\\Ranjit\\Documents')
# print(sys.argv[1:])
# print(os.stat('argvpythonexp.py'))
#
# print(os.chdir(path))
# print(os.getcwd())
# for dirpath, dirnames, filename in os.walk(os.getcwd()) :
#     print (dirpath, dirnames, filename)


def test_sysargs():
    sys.argv = ["prog", "-f", "/home/fenton/project/setup.py"]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    test_sysargs()

    print(sys.argv[1])

    parser.add_argument()
    (ars, data) = parser.parse_known_args()

    print(ars.prog)
