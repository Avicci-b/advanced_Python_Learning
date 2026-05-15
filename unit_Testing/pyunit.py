import unittest
import Area


class TestUnit(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Area.add(2,4),6)

unittest.main()