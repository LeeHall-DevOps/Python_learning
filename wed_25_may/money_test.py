from money import *
import unittest


class MoneyTest(unittest.TestCase):

    def test__init__(self):
        self.assertEqual(self.money_in(1000))

    def test__str__(self):
        self.assertEqual("You paid in £{self.money_in")

    def test__format__(self):
        assert self.money_in

    def test_display(self):
        assert customer_1


