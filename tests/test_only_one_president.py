import unittest

from singleton.america_president import AmericaPresident


class TestSingleton(unittest.TestCase):
    def test_only_one_president(self):
        self.assertEqual(AmericaPresident.PRESIDENT,
                         AmericaPresident.PRESIDENT)


if __name__ == '__main__':
    unittest.main()
