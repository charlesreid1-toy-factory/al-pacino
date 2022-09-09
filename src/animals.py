from abc import ABC


class Animal(ABC):
    """Base class"""

    def speak(self):
        raise NotImplementedError()

    def make_noise(self):
        print(self.noise)


class Cow(Animal):
    noise = "moo"


class Pig(Animal):
    noise = "oink"


class Dog(Animal):
    noise = "arf"


class Cat(Animal):
    noise = "mrkgnao"


class Human(Animal):
    noise = "buuurp"

    def speak(self):
        print("Hello world")
