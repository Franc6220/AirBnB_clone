#!/usr/bin/python3
# models/engine/file_storage.py
import json
from os.path import exists

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        if exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = key.split('.')[0]
                    # Import classes dynamically to avoid circular import
                    if class_name == "BaseModel":
                        from models.base_model import BaseModel
                        self.__objects[key] = BaseModel(**value)
                    # Add other classes here as needed

