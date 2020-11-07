from unittest import TestCase
from main import prime


class TestMain(TestCase):
    def test_prime(self):
        self.assertEqual(prime(1), False)
        self.assertEqual(prime(2), True)
        self.assertEqual(prime(3), True)
        self.assertEqual(prime(4), False)
        self.assertEqual(prime(5), True)
        self.assertEqual(prime(6), False)
        self.assertEqual(prime(7), True)
        self.assertEqual(prime(8), False)
        self.assertEqual(prime(9), False)
        self.assertEqual(prime(10), False)
        self.assertEqual(prime(11), True)
        self.assertEqual(prime(12), False)
        self.assertEqual(prime(13), True)
        self.assertEqual(prime(14), False)
        self.assertEqual(prime(15), False)
        self.assertEqual(prime(16), False)
        self.assertEqual(prime(17), True)
        self.assertEqual(prime(18), False)
        self.assertEqual(prime(19), True)
        self.assertEqual(prime(20), False)
        self.assertEqual(prime(21), False)
