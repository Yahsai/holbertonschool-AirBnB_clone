# tests/test_console.py
"""Unit test for console
    """
import unittest
from unittest.mock import patch
from console import HBNBCommand
import io

class TestConsole(unittest.TestCase):
    """TestConsole Class
    Args:
        unittest (): properties of unit test"""
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        """ destroys created file """
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

    # Add more test cases for other commands and functionalities

if __name__ == '__main__':
    unittest.main()
