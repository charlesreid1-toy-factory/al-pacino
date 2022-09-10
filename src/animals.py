class Animal(object):
    """Base class"""
    noise = None

    def make_noise(self):
        if self.noise is None:
            raise NotImplementedError()
        else:
            print(self.noise)


class Goat(Animal):
    noise = "baaa"


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
