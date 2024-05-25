#!/usr/bin/python3
#Defines base model class

from uuid import uuid4
from datetime import datetime


class BaseModel:
	#Represents base_model of HBnB project


	def __init__(self):
		#Public instance attributes
		self.id = str(uuid.uuid4())
		self.created_at = datetime.now()
		self.updated_at = self.created_at


	def __str__(self):
		#Returns str representation of the BaseModel
		class_name = self.__class__.__name
		return f"[{self._class_._name_}] ({self.id}) {self._dict_}"


	def save(self):
		#Modifies updated_at with current datetime. 
		self.updated_at = datetime.now()


	def to_dict(self):
		#Creates a dict of the self-set values
		dict_repr = self.__dict__.copy()
		dict_repr["__class__"] = self.__class__.__name__
		dict_repr["created_at"] = self.created_at.isoformat()
		dict_repr["updated_at"] = self.updated_at.isoformat()
		return dict_repr
