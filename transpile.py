import sys
import os
import argparse
import subprocess

from _version import __version__

def execute_cmd(cmd):
    """
    :param cmd: String
    :return: Boolean or String

    Executes a bash command passed to it in a shell, returns the result of the command or false if errored
    """
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if stderr:
        sys.exit(2)
    return stdout


def check_change(file, time=0.0):
    """
    :param file: Filepath String
    :param time: Float
    :return: Float or False

    Returns new mtime if an the file mtime has changed
    """
    if not os.path.isfile(file):
        sys.exit(1)

    mtime = os.path.getmtime(file)
    if  mtime > time:
       return mtime
    return False


def parse_args(args):
    """
    :param args: a list of command line arguments
    :return: populated namespace

    Takes a list of command line arguments and parse them, returning the poulated namespace
    """
    parser = argparse.ArgumentParser(
        description='A simple python transpiler to run a command whenver a file changes',
        epilog='Usage: python transpile.py -f README.md -c pandoc README.md > /tmp/README.html'
    )
    parser.add_argument('-f', '--file', action='store', required=True, help='The file path toe hte file to be watched for changes (changes means change in mtime')
    parser.add_argument('-c', '--command', action='store', required=True, help='The command to be run whenever the watched file changes')
    parser.add_argument('-v-', '--version', action='version', version='%(prog)s {version}'.format(version=__version__))
    return parser.parse_args(args)


def main_loop(file, cmd):
    """
    :param args:
    :return: None
    """
    time = 0.0
    try:
        while True:
            n_time = check_change(file, time)
            if n_time:
                execute_cmd(cmd)
                time = n_time
    except KeyboardInterrupt:
        sys.exit(3)

if __name__ == '__main__':
    args = parse_args(sys.argv[1:])
    main_loop(args.file, args.command)
