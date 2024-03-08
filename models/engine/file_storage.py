#!/usr/bin/python3
#Defines Class FileStorage
import json
from models.base_model import BaseModel

class FileStorage:
	#serializes instances to a JSON file and deserializes JSON file to instances
	__file_path = "file.json"
	__objects = {}

	def all(self):
		#returns the dictionary __objects
		return FileStorage._objects

	def new(self, obj):
		#sets in __objects the obj with key <obj class name>.id
		ocname = obj._class_._name_
		FileStorage._objects["{}.{}".format(ocname, obj.id)] = obj

	def save(self):
		#serializes __objects to the JSON file
		odict = {obj: odict[obj].to_dict() for obj in odict.keys()}
		with open(FileStorage._file_path, "w") as f:
			json.dump(objdict, f)

	def reload(self):
		"""deserializes the JSON file to __objects (only if the JSON file (__file_path) exists ; otherwise, do nothing. If the file doesn’t exist, no exception should be raised)"""
		try:
			with open(FileStorage._file_path) as f:
				objdict = json.load(f)
				for o in objdict.values():
					class_name = o["_class_"]
					del o["_class_"]
					self.new(eval(class_name)(**o))
		except FileNotFoundError:
			 
