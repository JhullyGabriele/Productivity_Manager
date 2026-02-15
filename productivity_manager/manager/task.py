#Task

import uuid
from datetime import datetime

class Task:
	def __init__(self, title, description, priority, due_date, category):
		self._id = str(uuid.uuid4())
		self._title = title
		self.description = description
		self.priority = priority
		self._due_date = due_date
		self.category = category
		self._completed = False
		self._created_at = datetime.now()

#Início do encapsulamento

	@property
	def title(self):
		return self._title

	@title.setter
	def title(self, value):
		if not value:
			raise ValueError("Título não pode ser vazio.")
		self._title = value

	@property
	def completed(self):
		return self._completed

	def mark_completed(self):
		self._completed = True

	@property
	def due_date(self):
		return self._due_date

	@due_date.setter
	def due_date(self, value):
		self._due_date = value

	@property
	def id(self):
		return self._id

	@property
	def created_at(self):
		return self._created_at

#Fim do encapsulamento
