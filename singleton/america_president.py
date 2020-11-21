from pypattyrn.creational.singleton import Singleton

class AmericaPresident(object, metaclass=Singleton):
    @classmethod
    def getInstance(self) -> Singleton:
        return AmericaPresident()
    def say_something(self) -> None:
        return "I'm the only president of the United States."
