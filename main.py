from singleton.america_president import AmericaPresident


class App:
    def main():
        trump = AmericaPresident()
        print(id(trump))
        print(trump.say_something())
        biden = AmericaPresident()
        print(id(biden))
        print(biden.say_something())


if __name__ == '__main__':
    App.main()
