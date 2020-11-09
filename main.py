from singleton.america_president import AmericaPresident


class App:
    def main():
        trump = AmericaPresident()
        print(id(trump))
        print(trump.say_something())
        joe = AmericaPresident()
        print(id(joe))
        print(joe.say_something())


App.main()
