from singleton.america_president import AmericaPresident

class App:
  def main():
    trump = AmericaPresident()
    print(id(trump))
    trump.do_something()
    joe = AmericaPresident()
    print(id(joe))
    joe.do_something()

App.main()