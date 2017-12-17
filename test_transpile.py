"""
MIT License

Copyright (c) 2017 Oliver Sealey

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""



import unittest
import mock
import sys
from os.path import getmtime

from transpile import parse_args, execute_cmd, check_change, main_loop



class ParserTest(unittest.TestCase):
    def test_parser_two_short_arguments(self):
        """
        Tests that the parser works correctly when parsed two arguments and two flags
        """
        parser = parse_args(['-f', 'file1', '-c', 'command1'])
        self.assertEqual(parser.file, 'file1')
        self.assertEqual(parser.command, 'command1')

    def test_parser_two_long_arguments(self):
        """
        Tests that the parser works correctly when parsed two arguments and two flags
        """
        parser = parse_args(['--file', 'file1', '--command', 'command1'])
        self.assertEqual(parser.file, 'file1')
        self.assertEqual(parser.command, 'command1')

class ExecuteCmdTest(unittest.TestCase):
    def test_execute_cmd_echo(self):
        """
        Tests the output for the uname command
        """
        cmd = '(exit 1) | echo running the test'
        self.assertEqual(execute_cmd(cmd), 'running the test\n')

    def test_execute_cmd_illigal_cmd(self):
        """
        Tests the execute command procides false on illegal commands
        """
        cmd = 'not a command'
        with self.assertRaises(SystemExit) as se:
            execute_cmd(cmd)

        self.assertEqual(se.exception.code, 2)

class CheckFileTest(unittest.TestCase):
    def test_check_file_sys_exit(self):
        """
        Checks that an invalid file causes a sys.exit
        """
        file = '//this/file/does/not/exist'
        with self.assertRaises(SystemExit) as se:
            check_change(file)

        self.assertEqual(se.exception.code, 1)

    def mock_getmtime(self):
        return 1234.5

    @mock.patch('os.path.getmtime', side_effect=mock_getmtime)
    def test_check_file_with_change(self, check_change_function):
        """
        Test that a file that has changed returns the new time
        """
        file = '//bin//ls'
        self.assertEqual(check_change(file, 0.0), 1234.5)

    @mock.patch('os.path.getmtime', side_effect=mock_getmtime)
    def test_check_file_time_equal(self, check_change_function):
        """
        Tests that a file with the newer time returns False
        """
        file = '//bin//ls'
        self.assertFalse(check_change(file, 1234.5))


    def test_check_file_newer(self):
        """
        Tests that a file with the newer time returns False
        """
        file = '//bin//ls'
        self.assertFalse(check_change(file, sys.float_info.max))

if __name__ == '__main__':
    unittest.main()