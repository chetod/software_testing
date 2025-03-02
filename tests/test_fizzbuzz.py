import unittest
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    def test_fizzbuzz_divisible_by_3_and_5(self):
        self.assertEqual(fizzbuzz(15), "FizzBuzz")  # 15 หารด้วย 3 และ 5 ลงตัว
        self.assertEqual(fizzbuzz(30), "FizzBuzz")  # 30 หารด้วย 3 และ 5 ลงตัว

    def test_fizzbuzz_divisible_by_3(self):
        self.assertEqual(fizzbuzz(3), "Fizz")  # 3 หารด้วย 3 ลงตัว
        self.assertEqual(fizzbuzz(9), "Fizz")  # 9 หารด้วย 3 ลงตัว

    def test_fizzbuzz_divisible_by_5(self):
        self.assertEqual(fizzbuzz(5), "Buzz")  # 5 หารด้วย 5 ลงตัว
        self.assertEqual(fizzbuzz(10), "Buzz")  # 10 หารด้วย 5 ลงตัว

    def test_fizzbuzz_not_divisible_by_3_or_5(self):
        self.assertIsNone(fizzbuzz(2))  # 2 ไม่หารด้วย 3 หรือ 5 ลงตัว
        self.assertIsNone(fizzbuzz(7))  # 7 ไม่หารด้วย 3 หรือ 5 ลงตัว

