from abc import ABC, abstractmethod

class user(ABC):
    def __init__(self, name, password):
        self._name = name
        self._password = password

    @abstractmethod
    def login(self, password):
        raise NotImplementedError
    
    @abstractmethod
    def edit_password(self, new_password):
        raise NotImplementedError
    
    @property
    def name(self):
        return self._name
