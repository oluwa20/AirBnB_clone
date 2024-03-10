from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage

class HBNBCommand(cmd.Cmd):
    """Command interpreter class"""

    prompt = "(hbnb) "

    def do_show(self, arg):
        """Show command"""
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = "{}.{}".format(args[0], args[1])
        if obj_key not in storage.all():
            print("** no instance found **")
            return
        print(storage.all()[obj_key])

    def do_create(self, arg):
        """Create command"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_obj = eval(arg)()
            new_obj.save()
            print(new_obj.id)
        except:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Destroy command"""
        args = arg.split()
        if len(args) < 2:
            print("** instance id missing **")
            return
        obj_key = "{}.{}".format(args[0], args[1])
        if obj_key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[obj_key]
        storage.save()

    def do_update(self, arg):
        """Update command"""
        args = arg.split()
        if len(args) < 3:
            print("** instance id missing **")
            return
        obj_key = "{}.{}".format(args[0], args[1])
        if obj_key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 4:
            print("** attribute name missing **")
            return
        if len(args) < 5:
            print("** value missing **")
            return
        obj = storage.all()[obj_key]
        setattr(obj, args[3], args[4])
        obj.save()

    def do_all(self, arg):
        """All command"""
        objs = []
        if not arg:
            for obj in storage.all().values():
                objs.append(obj)
        else:
            try:
                objs = [obj for obj in storage.all().values() if type(obj).__name__ == arg]
            except:
                print("** class doesn't exist **")
                return
        print(objs)

    def do_quit(self, arg):
        """Quit command"""
        raise SystemExit

    def do_EOF(self, arg):
        """EOF command"""
        print("")
        raise SystemExit

    def emptyline(self):
        """Empty line"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
