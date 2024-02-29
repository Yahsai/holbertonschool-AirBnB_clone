#!/usr/bin/python3
#!/usr/bin/env python3
"""
Console module for the AirBnB project.
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter.
    """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF (Ctrl-D)."""
        print("")  # New line for better formatting
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
