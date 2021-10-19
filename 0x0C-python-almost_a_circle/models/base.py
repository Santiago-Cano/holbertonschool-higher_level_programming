#!/usr/bin/python3
"""Contains Base class, which will function as the base of all other classes"""

import json
import csv


class Base:
    """ Class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Constructor of Base class

        Args:
             id: id of each instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        filename = cls.__name__ + ".json"
        list = []
        if list_objs is not None:
            for i in list_objs:
                list.append(cls.to_dictionary(i))
        with open(filename, 'w') as json_file:
            json_file.write(cls.to_json_string(list))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Square":
            dummy = cls(7)
        elif cls.__name__ == "Rectangle":
            dummy = cls(7, 7)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        file = cls.__name__ + ".json"
        list = []
        try:
            with open(file, mode="r") as f:
                readfile = cls.from_json_string(f.read())
                for i in readfile:
                    list.append(cls.create(**i))
                return (list)
        except:
            pass
        return []

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes a CSV file"""
        file = cls.__name__ + ".csv"
        list = []

        try:
            with open(file, mode="r") as f:
                readfile = csv.reader(f)
                for i in readfile:
                    if cls.__name__ == "Rectangle":
                        dict = {
                            "id": int(i[0]),
                            "width": int(i[1]),
                            "height": int(i[2]),
                            "x": int(i[3]),
                            "y": int(i[4])
                        }
                    if cls.__name__ == "Square":
                        dict = {
                            "id": int(i[0]),
                            "size": int(i[1]),
                            "x": int(i[2]),
                            "y": int(i[3])
                        }
                    list.append(cls.create(**dict))
        except:
            pass
        return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes a CSV file"""
        file = cls.__name__ + ".csv"

        with open(file, mode='w') as f:
            writefile = csv.writer(f)
            if cls.__name__ == "Rectangle":
                for i in list_objs:
                    writefile.writerow([i.id, i.width, i.height, i.x, i.y])
            if cls.__name__ == "Square":
                for i in list_objs:
                    writefile.writerow([i.id, i.size, i.x, i.y])
