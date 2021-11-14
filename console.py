#!/usr/bin/python3
'''
the entry point of the command interpreter
'''

import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import sys
import inspect


class HBNBCommand(cmd.Cmd):
    '''
    command line interpreter class
    '''

    prompt = '(hbnb)'

    def get_classes(self):
        all_classes = []
        for name, obj in inspect.getmembers(sys.modules[__name__]):
            if inspect.isclass(obj):
                all_classes.append("{}".format(obj.__name__))
        return all_classes

    def emptyline(self):
        pass

    def do_EOF(self, arg):
        '''
        quits the command interpreter
        '''
        return True

    def do_quit(self, arg):
        '''
        quits the command interpreter
        '''
        return True

    def do_create(self, args):
        '''
        Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        '''
        if not args:
            print('** class name missing **')
            return False
        if args not in globals():
            print("** class doesn't exist **")
            return False
        Class = globals()[args]
        new_obj = Class()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arg):
        '''
        Prints the string representation of an instance based on
        the class name and id
        Usage:
            show <BaseModel> <9bffd505-c163-40ce-a210-c9dd1cda9409>
        '''
        if arg:
            args = arg.split(' ')
            if len(args) != 2:
                if not args[0] in globals():
                    print("** class doesn't exist **")
                    return False
                print('** instance id missing **')
                return False
            Class = globals()[args[0]]
            key = ".".join(args)
            objects = models.storage.all()
            if key not in objects:
                print('** no instance found **')
                return False
            new_obj = Class(**objects[key])
            print(new_obj)

        else:
            print('** class name missing **')
            return False

    def do_destroy(self, arg):
        '''
        Deletes an instance based on the class name and id
        (save the change into the JSON file).
        Usage:
            $ destroy BaseModel 1234-1234-1234
        '''
        if not arg:
            print('** class name missing **')
            return False
        args = arg.split()
        if args[0] not in globals():
            print('** class doesn\'t exist **')
            return False
        if len(args) != 2:
            print('** instance id missing **')
            return False
        Class = globals()[args[0]]
        key = ".".join(args)
        objs = models.storage.all()
        if key not in objs:
            print("** no instance found **")
            return False

        del objs[key]
        models.storage.save()

    def do_all(self, args):
        '''
        Prints all string representation of all instances
        based or not on the class name.

        Usage:
            (hbnb)all BaseModel   or    (hbnb)all
        '''
        str_list = []
        if len(args) == 0:
            all_dict = models.storage.all()
            for id in all_dict.keys():
                obj = all_dict[id]
                idx = id.split('.')
                Class = globals()[idx[0]]
                str_list.append("{}".format(Class(**obj)))
            print(str_list)
        else:
            models.storage.reload()
            args = args.split()
            if args[0] in globals():
                all_dict = models.storage.all()
                Class = globals()[args[0]]
                for id in all_dict.keys():
                    if args[0] in id:
                        obj = Class(**all_dict[id])
                        str_list.append("{}".format(obj))
                print(str_list)
            else:
                print("** class doesn't exist **")
                return False

    def do_update(self, args):
        '''
        Updates an instance based on the class name and id
        by adding or updating attribute

        Usage:
            update <class name> <id> <attribute name> "<attribute value>"
        '''
        if len(args) == 0:
            print("** class name missing **")
            return False
        args = args.split()
        if args[0] not in globals():
            print("** class doesn't exist **")
            return False
        Class = globals()[args[0]]
        if len(args) < 2:
            print("** instance id missing **")
            return False
        all_objects = models.storage.all()
        key = ".".join([args[i] for i in range(2)])
        if key not in all_objects:
            print("** no instance found **")
            return False
        if len(args) < 3:
            print("** attribute name missing **")
            return False
        if len(args) < 4:
            print("** value missing **")
            return False
        all_objects[key][args[2]] = args[3]
        new_obj = Class(**all_objects[key])
        new_obj.save()
    def do_(self, args):
        """
        test
        """

        print('123456')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
