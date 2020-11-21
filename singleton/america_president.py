from pypattyrn.creational.singleton import Singleton

class AmericaPresident(object, metaclass=Singleton):
    def say_something(self) -> None:
        return "I'm the only president of the United States."
