#!/usr/bin/env python3
'''base_model module
'''
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
	"""base model class"""

	def __init__(self, *args, **kwargs):
		if kwargs:
			for k, v in kwargs.items():
				if k != '__class__':
					val = None
					if k == 'updated_at' or k == 'created_at':
						val = datetime.fromisoformat(v)
						setattr(self, k, val)
					else:
						setattr(self, k, v)

		else:
			self.id = str(uuid4())
			self.created_at = datetime.utcnow()
			self.updated_at = datetime.utcnow()
			models.storage.new(self)

	def __str__(self):
		return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

	def save(self):
		self.updated_at = datetime.utcnow()
		models.storage.save()

	def to_dict(self):
		obj = self.__dict__.copy()
		obj['__class__'] = self.__class__.__name__
		obj['updated_at'] = obj['updated_at'].isoformat()
		obj['created_at'] = obj['created_at'].isoformat()
		return obj
