from abc import ABC, abstractmethod

class Pysics(ABC):
    @abstractmethod
    def collision(self, other):
        pass

    @abstractmethod
    def gravity(self):
        pass

    @abstractmethod
    def coordinates(self):
        pass

    @abstractmethod
    def border(self):
        pass