# Create basemodel class with the following attributes:
# 1. id
# 2. created_at
# 3. upated_at
# 4. __str__: should print: [<class name>] (<self.id>) <self.__dict__>
# and the following methods:
# 5. save: updates the public instance attribute updated_at with the current
#datetime
# 6. to_dict: returns a dictionary copy of the instance
# crreated_at and updated_at must be converted to string object in ISO format:
#f ormat: %Y-%m-%dT%H:%M:%S.%f (ex: 2017-06-14T22:31:03.285259)
# you can use isoformat() of datetime object

from datetime import datetime
import uuid
import os

class Basemodel
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    def __str__(self):
        return "({}) ({}) {}".format(self.__class__.__name__. self.id, self.__dict__)
    
    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        iso_time = "%Y-%m-%dT%H:%M:%S.%f"
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.strftime(iso_time)
        rdict["updated_at"] = self.updated_at.strftime(iso_time)
        rdict["__class__"] = self.__class__.__name__
        return rdict