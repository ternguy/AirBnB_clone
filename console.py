#!/usr/bin/python3
""" The entry point of the command interpreter """

import cmd
import re
from models import storage
from shlex import split
from models.base_model import BaseModel

def parse(arg):
    """ Create the parce method """
    guilemets = re.search(r"\{(.*?)\}", arg)
    crochets = re.search(r"\[(.*?)\]", arg)
    if guilemets is None:
        if crochets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:crochets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(crochets.group())
            return retl
    else:
        lexer = split(arg[:guilemets.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(guilemets.group())
        return retl

class HBNBCommand(cmd.Cmd):
    """ The class airbnb command line interpreter """

    prompt = "(hbnb) "
    __classes = {"BaseModel"}

    def do_quit(self, arg):
        """ Exit the program """

        return True

    def do_EOF(self, arg):
        """ Quit the program by end of file """

        print("")
        return True
    
    def emptyline(self):
        """ When the empty line is entered """
        
        pass
    def do_create(self, line):
        """ Create a new instance of the BaseModel and print the id
        if the class name is missing, print that it is missing
        if the class doesn't exist, print that it doesn't exist
        """

        try:
            if not line:
                raise SyntaxError()
            the_list = line.split(" ")

            kwargs = {}
            for i in range(1, len(the_list)):
                key, value = tuple(the_list[i].split("="))
                if value[0] == '"':
                    value = value.strip('"').replace("_", " ")
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                kwargs[key] = value

            if kwargs == {}:
                obj = eval(the_list[0])()
            else:
                obj = eval(the_list[0])(**kwargs)
                storage.new(obj)
            print(obj.id)
            obj.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """ Showthe string representation of an instance based on the class name
        Ex:
            '$ show BaseModel 1234-1234-1234'
        """

        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])]

    def do_destroy(self, arg):
        """ Delete the class intance of a cetain id """

        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """ Prints all string representation of all instances
        based or not on the class name
        It must be a list of strings
        """

        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id by adding
        or updating the attribute
        """

        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

if __name__ == '__main___':
    HBNBCommand().cmdloop()
