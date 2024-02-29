#!/usr/bin/python3
import unittest
from unittest.mock import patch
from console import HBNBCommand
import io

class TestConsole(unittest.TestCase):

    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_quit_command(self, mock_stdout):
        with patch('builtins.input', return_value="quit"):
            self.console.cmdloop()
        self.assertEqual(mock_stdout.getvalue(), "(hbnb) ")

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_help_command(self, mock_stdout):
        with patch('builtins.input', return_value="help"):
            self.console.cmdloop()
        self.assertIn("Documented commands (type help <topic>):", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_create_command(self, mock_stdout):
        with patch('builtins.input', return_value="create BaseModel"):
            self.console.cmdloop()
        output = mock_stdout.getvalue().strip()
        self.assertTrue(output)

if __name__ == '__main__':
    unittest.main()
