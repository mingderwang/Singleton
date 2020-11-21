class Singleton(object):
    _instance = None

    def __new__(class_, *args, **kwargs):
        if not isinstance(class_._instance, class_):
            class_._instance = object.__new__(class_, *args, **kwargs)
        return class_._instance


class AmericaPresident(Singleton):
    @classmethod
    def getInstance(self):
        return AmericaPresident()

    def say_something(self) -> None:
        return "I'm the only president of the United States."
