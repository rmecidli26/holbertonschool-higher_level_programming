from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        """Bu metod alt siniflər tərəfindən mütləq tətbiq edilməlidir."""
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"
