#!/usr/bin/python3
#Defines base model class

from uuid import uuid4
from datetime import datetime

class BaseModel:
	#Represents base_model of HBnB project

	def __init__(self):
		#
		pass

	def save(self):
		#Modifies updated_at with current datetime. 
		self.updated_at = datetime.utcnow()
		models.storage.save()

	def to_dict(self):
		#Creates a dict of the self-set values
		result_dict = self.__dict__.copy()
		result_dict["__class__"] =self.__class__.__name__
		result_dict["created_at"] = self.created_at.isoformat()
		result_dict["updated_at"] = self.updated_at.isoformat()
		return result_dict

	def __str__(self):
		#Returns str representation of the BaseModel
		class_name = self.__class__.__name__
		return "[{}] ({}) {}".format(class_name, self.id, self._dict_)
