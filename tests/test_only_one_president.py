import unittest

from singleton.america_president import AmericaPresident


class TestSingleton(unittest.TestCase):
    def test_only_one_president(self):
        self.assertEqual(AmericaPresident.PRESIDENT,
                         AmericaPresident.PRESIDENT)


class TestSaySomthing(unittest.TestCase):
    def test_say_something(self):
        self.assertEqual("I'm the only president of the United States.",
                         AmericaPresident.PRESIDENT.say_something())


if __name__ == '__main__':
    unittest.main()
