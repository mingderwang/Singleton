from singleton.america_president import AmericaPresident


class App:
    def main():
        trump = AmericaPresident.PRESIDENT
        print(id(trump))
        print(trump.say_something())
        joe = AmericaPresident.PRESIDENT
        print(id(joe))
        print(joe.say_something())


App.main()
