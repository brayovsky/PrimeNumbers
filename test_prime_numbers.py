#has test cases for the function generate_prime_numbers.py

import unittest
import generate_prime_numbers


class TestPrimeNumberGeneration(unittest.TestCase):

    def test_integer(self):
        self.assertEqual(generate_prime_numbers.generate_prime_numbers(25),[2,3,5,7,11,13,17,19,23])

    # def test_negative(self):
    #     with self.assertRaises(generate_prime_numbers.NegativeNumberError):
    #         generate_prime_numbers.generate_prime_numbers(-7)

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()