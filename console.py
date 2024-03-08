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


	if __name__ == '__main__':
		HBNBCommand().cmdloop()
