#!/usr/bin/python3
#contains the entry point of the command interpreter
import cmd


class HBNBCommand(cmd.Cmd):
	#Defines Command Interpreter

	prompt = "(hbnb)"
	valid_classes = ["BaseModel"]

	def emptyline(self):
		#shouldn’t execute anything
		pass

	def do_quit(self, arg):
		#to exit the program
		return True
	
	def help_quit(self, arg):
		#Quit command to exit the program
		return True

	def do_EOF(self, arg):
		#End Of File
		return True

	def do_create(self, arg):
		#Creates a new instance of BaseModel, saves it to the JSON file and prints the id
		class_name = arg
		if len(class_name) == 0:
			print("** class name missing **")
		elif class_name[0] not in HBNBCommand._classes:
			print("** class dosen't exist **")
		else:
			print(eval(class_name[0])().id)
			storage.save()




if __name__ == '__main__':
	HBNBCommand().cmdloop()
