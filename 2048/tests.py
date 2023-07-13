import unittest
from main import get_number_from_index

class Test2048(unittest.TestCase):

    def test_1(self):
        self.assertEqual(2, 1 + 1)
    def test_2(self):
        self.assertEqual(get_number_from_index(1,2), 7)
