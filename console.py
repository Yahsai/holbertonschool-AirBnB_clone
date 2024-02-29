#!/usr/bin/env python3
"""
Console module for the AirBnB project.
"""

import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class for the command interpreter.
    """
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on empty line."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """Exit the program with EOF (Ctrl-D)."""
        print("")  # New line for better formatting
        return True

    def check_class(self, class_name):
        """Check if class exists."""
        try:
            cls = eval(class_name)
            return True
        except NameError:
            return False

    def check_id(self, class_name, instance_id):
        """Check if instance id exists."""
        key = "{}.{}".format(class_name, instance_id)
        objects = storage.all()
        return key in objects

    def do_create(self, arg):
        """Creates a new instance of BaseModel."""
        if not arg:
            print("** class name missing **")
            return

        if not self.check_class(arg):
            print("** class doesn't exist **")
            return

        new_instance = eval(arg)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if not self.check_class(args[0]):
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        if not self.check_id(args[0], args[1]):
            print("** no instance found **")
            return

        key = "{}.{}".format(args[0], args[1])
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if not self.check_class(args[0]):
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        if not self.check_id(args[0], args[1]):
            print("** no instance found **")
            return

        key = "{}.{}".format(args[0], args[1])
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances."""
        args = arg.split()
        objects = storage.all()
        result = []

        if not arg:
            for key, value in objects.items():
                result.append(str(value))
            print(result)
        else:
            if not self.check_class(args[0]):
                print("** class doesn't exist **")
                return

            for key, value in objects.items():
                if key.split(".")[0] == args[0]:
                    result.append(str(value))
            print(result)

    def do_update(self, arg):
        """Updates an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        if not self.check_class(args[0]):
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        if not self.check_id(args[0], args[1]):
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        obj = storage.all()[key]
        setattr(obj, args[2], eval(args[3]))
        obj.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
