from singleton.america_president import AmericaPresident


class App:
    def main():
        a = AmericaPresident()
        b = AmericaPresident.getInstance()
        c = a.getInstance()
        print(id(a))
        print(id(b))
        print(id(c))


if __name__ == '__main__':
    App.main()
