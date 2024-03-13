#!/usr/bin/python3
#Defines base model class

from uuid import uuid4
from datetime import datetime


instance1 = ["{str(uuid.uuid4)}", "datetime.utcnow", "datetime.utcnow"]
instance2 = ["{str(uuid.uuid4)}", "datetime.utcnow", "datetime.utcnow"]


class BaseModel:
	#Represents base_model of HBnB project


	def __init__(self, id, created_at, updated_at):
		#Public instance attributes
		self.id = id
		self.created_at = created_at
		self.updated_at = updated_at


	def code(self):
		print(f"{self.id}, {self.created_at}, {self.updated_at} is first instance")


		instance1 = BaseModel("{str(uuid.uuid4)}", "datetime.utcnow", "datetime.utcnow")
		instance2 = BaseModel("{str(uuid.uuid4)}", "datetime.utcnow", "datetime.utcnow")

		instance1.code()
		instance2.code()


	def save(self):
		#Modifies updated_at with current datetime. 
		self.updated_at = datetime.utcnow()
		models.storage.save()


	def to_dict(self):
		#Creates a dict of the self-set values
		return_dict = self.__dict__.copy()
		return_dict["__class__"] = self.__class__.__name__
		return_dict["created_at"] = self.created_at.isoformat()
		return_dict["updated_at"] = self.updated_at.isoformat()
		return return_dict


	def __str__(self):
		#Returns str representation of the BaseModel
		class_name = self.__class__.__name__
		return "[{}] ({}) {}".format(class_name, self.id, self._dict_)
