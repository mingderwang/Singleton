import enum


class AmericaPresident(enum.Enum):
    PRESIDENT = ''

    def say_something(self):
        return "I'm the only president of the United States."