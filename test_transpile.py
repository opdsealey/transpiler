import unittest

from transpile import parse_args, execute_cmd

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
        self.assertFalse(execute_cmd(cmd))

if __name__ == '__main__':
    unittest.main()