#!/usr/bin/python3
"""
This is the console module for the AirBnB clone project.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    This class defines the command interpreter for the console.
    """

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        Handles EOF (Ctrl + D) to exit the program.
        """
        print("")
        return True

    def emptyline(self):
        """
        Handles empty line to do nothing.
        """
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
