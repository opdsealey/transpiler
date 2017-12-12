import sys
import os
import argparse
import subprocess

from _version import __version__

def execute_cmd(cmd):
    """
    :param cmd: String
    :return: Boolean

    Executes a bash command passed to it in a shell, returns the result of the command or false if errored
    """
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if stderr:
        return False
    return stdout



def check_change(file, time):
    """

    :param file: String
    :param time: Time Object
    :return: Boolean

    Returns true if an the file mtime has changed
    """

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

if __name__ == '__main__':
    args = ['--version']

    a = parse_args(args)
    pass