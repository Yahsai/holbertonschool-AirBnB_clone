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

import unittest
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):

    def setUp(self):
        """Set up for the tests"""
        self.cmd = HBNBCommand()

    def test_instantiation(self):
        """Test instantiation of HBNBCommand"""
        self.assertIsInstance(self.cmd, HBNBCommand)

    # def test_quit(self):
    #     """Test quit command"""
    #     with self.assertRaises(SystemExit):
    #         self.cmd.do_quit(None)


if __name__ == '__main__':
    unittest.main()

if __name__ == '__main__':
    unittest.main()
