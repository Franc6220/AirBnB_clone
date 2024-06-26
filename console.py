#!/usr/bin/env python3
import cmd
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    classes = {
        "BaseModel": BaseModel, "User": User, "State": State,
        "City": City, "Amenity": Amenity, "Place": Place, "Review": Review
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of a model, saves it (to the JSON file) and prints the id."""
        if not arg:
            print("** class name missing **")
            return
        if arg not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[arg]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and id."""
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
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)."""
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
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name."""
        if arg and arg not in self.classes:
            print("** class doesn't exist **")
            return
        result = []
        for key, value in storage.all().items():
            if not arg or key.startswith(arg + "."):
                result.append(str(value))
        print(result)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute."""
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
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return

        instance = storage.all()[key]
        attr_name = args[2]
        attr_value = args[3].strip('"')

        # Cast value to the correct type
        if hasattr(instance, attr_name):
            attr_type = type(getattr(instance, attr_name))
            try:
                attr_value = attr_type(attr_value)
            except ValueError:
                print(f"** wrong type for {attr_name} **")
                return

        setattr(instance, attr_name, attr_value)
        instance.save()

    def do_count(self, class_name):
        """Counts the number of instances of a class."""
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        count = sum(1 for key in storage.all() if key.startswith(class_name + "."))
        print(count)

    def default(self, line):
        """Handle commands with syntax <class name>.all(), <class name>.count(), <class name>.show(<id>), <class name>.destroy(<id>), <class name>.update(<id>, <attribute name>, <attribute value>), <class name>.update(<id>, <dictionary representation>)"""
        if "." in line:
            parts = line.split(".")
            class_name = parts[0]
            command = parts[1]

            if class_name in self.classes:
                if command == "all()":
                    self.do_all(class_name)
                elif command == "count()":
                    self.do_count(class_name)
                elif command.startswith("show(") and command.endswith(")"):
                    id_arg = command[5:-1]
                    self.do_show(f"{class_name} {id_arg}")
                elif command.startswith("destroy(") and command.endswith(")"):
                    id_arg = command[8:-1]
                    self.do_destroy(f"{class_name} {id_arg}")
                elif command.startswith("update(") and command.endswith(")"):
                    args = command[7:-1].split(", ", 1)
                    if len(args) == 2:
                        id_arg = args[0]
                        if args[1].startswith("{") and args[1].endswith("}"):
                            try:
                                attr_dict = json.loads(args[1])
                                self.update_from_dict(class_name, id_arg, attr_dict)
                            except json.JSONDecodeError:
                                print(f"*** Unknown syntax: {line}")
                        else:
                            attr_name, attr_value = args[1].split(", ", 1)
                            self.do_update(f"{class_name} {id_arg} {attr_name} {attr_value}")
                    else:
                        print(f"*** Unknown syntax: {line}")
                else:
                    print(f"*** Unknown syntax: {line}")
            else:
                print(f"*** Unknown syntax: {line}")

    def update_from_dict(self, class_name, id_arg, attr_dict):
        """Updates an instance based on class name and id using a dictionary of attributes."""
        key = class_name + "." + id_arg
        if key not in storage.all():
            print("** no instance found **")
            return

        instance = storage.all()[key]
        for attr_name, attr_value in attr_dict.items():
            # Cast value to the correct type
            if hasattr(instance, attr_name):
                attr_type = type(getattr(instance, attr_name))
                try:
                    attr_value = attr_type(attr_value)
                except ValueError:
                    print(f"** wrong type for {attr_name} **")
                    continue
            setattr(instance, attr_name, attr_value)
        instance.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()

