from singleton.america_president import AmericaPresident


class App:
    def main():
        a = AmericaPresident()
        b = AmericaPresident()
        print(id(a))
        print(id(b))


if __name__ == '__main__':
    App.main()
