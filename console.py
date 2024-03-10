#!/usr/bin/python3
#contains the entry point of the command interpreter
import cmd

class HBNBCommand(cmd.Cmd):
	#Defines Command Interpreter

	prompt = "(hbnb)"

	def emptyline(self):
		#shouldn’t execute anything
		pass

	def do_quit(self, arg):
		#to exit the program
		return TRUE

	def do_EOF(self, arg):
		#End Of File
		return TRUE

	def do_create(self, arg):
		#Creates a new instance of BaseModel, saves it to the JSON file and prints the id
		class_name = parser(arg)
		if len(class_name) == 0:
			print("** class name missing **")
		elif class_name[0] not in HBNBCommand._classes:
			print("** class dosen't exist **")
		else:
			print(eval(class_name[0])().id)
			storage.save()

	def do_show(self, arg):	


	if __name__ == '__main__':
		HBNBCommand().cmdloop()
