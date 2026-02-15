import uuid

class Category:
    def __init__(self, name, color):
        self._id = str(uuid.uuid4())
        self._name = name
        self.color = color

    # Início do encapsulamento
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
    # Fim do encapsulamento

