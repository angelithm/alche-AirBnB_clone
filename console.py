#!/usr/bin/python3
"""Entry point of the command interpreter."""
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import models


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the Airbnb project."""

    prompt = "(hbnb) "

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, arg):
        """Quit the console."""
        return True

    def do_EOF(self, arg):
        """Exit the console using EOF."""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, arg):
        """Create a new instance of a class."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        instance = self.classes[class_name]()
        instance.save()
        print(instance.id)

    def do_show(self, arg):
        """Show an instance by class name and ID."""
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        instance = models.storage.all().get(key)

        if instance is None:
            print("** no instance found **")
        else:
            print(instance)

    def do_destroy(self, arg):
        """Delete an instance by class name and ID."""
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])

        if key not in models.storage.all():
            print("** no instance found **")
            return

        del models.storage.all()[key]
        models.storage.save()

    def do_all(self, arg):
        """Print all instances or instances of a specified class."""
        args = arg.split()
        objects = models.storage.all()

        if args and args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if args:
            result = [
                str(obj) for obj in objects.values()
                if obj.__class__.__name__ == args[0]
            ]
        else:
            result = [str(obj) for obj in objects.values()]

        print(result)

    def do_update(self, arg):
        """Update an instance's attributes."""
        args = arg.split()

        if not args:
            print("** class name missing **")
            return

        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        instance = models.storage.all().get(key)

        if instance is None:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute = args[2]
        value = args[3]

        if attribute not in ("id", "created_at", "updated_at"):
            current_value = getattr(instance, attribute, None)

            if current_value is not None:
                value = type(current_value)(value)

            setattr(instance, attribute, value)

        instance.save()

    def default(self, line):
        """Handle class-based command syntax."""
        match = re.match(
            r"^(\w+)\.(all|count|show|destroy|update)\((.*)\)$",
            line
        )

        if not match:
            print("*** Unknown syntax: {}".format(line))
            return

        class_name, command, arguments = match.groups()

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if command == "all":
            self.do_all(class_name)
        elif command == "count":
            count = sum(
                1 for obj in models.storage.all().values()
                if obj.__class__.__name__ == class_name
            )
            print(count)
        elif command == "show":
            obj_id = re.search(r"""["']([^"']+)["']""", arguments)
            if obj_id:
                self.do_show("{} {}".format(class_name, obj_id.group(1)))
        elif command == "destroy":
            obj_id = re.search(r"""["']([^"']+)["']""", arguments)
            if obj_id:
                self.do_destroy("{} {}".format(class_name, obj_id.group(1)))
        elif command == "update":
            values = re.findall(r"""["']([^"']+)["']""", arguments)
            if len(values) >= 3:
                self.do_update(
                    "{} {} {} {}".format(
                        class_name, values[0], values[1], values[2]
                    )
                )


if __name__ == "__main__":
    HBNBCommand().cmdloop()
