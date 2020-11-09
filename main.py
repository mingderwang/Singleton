from singleton.america_president import AmericaPresident


class App:
    def main():
        trump = AmericaPresident.PRESIDENT
        print(id(trump))
        trump.do_something()
        joe = AmericaPresident.PRESIDENT
        print(id(joe))
        joe.do_something()


App.main()
