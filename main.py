from singleton.america_president import AmericaPresident, Logger


class App:
    def main():
        trump = AmericaPresident()
        print(id(trump))
        print(trump.say_something())

        biden = AmericaPresident()
        print(id(biden))
        print(biden.say_something())

        print(trump.say_something())

        log = Logger()
        print(id(log))
        log2 = Logger()
        print(id(log2))
        log2.log()


if __name__ == '__main__':
    App.main()
