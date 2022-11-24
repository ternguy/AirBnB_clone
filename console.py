#!/usr/bin/python3
""" The entry point of the command interpreter """

import cmd

class HBNBCommand(cmd.Cmd):
    """ The class airbnb command line interpreter """

    prompt = "(hbnb) "
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

if __name__ == '__main___':
    HBNBCommand().cmdloop()
