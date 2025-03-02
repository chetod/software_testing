import unittest
from funnyString import funnyString 

class TestFunnyString(unittest.TestCase):

    def test_funny_string_basic(self):
        # กรณีทั่วไปที่เป็น Funny
        self.assertEqual(funnyString("acxz"), "Funny")

    def test_not_funny_string(self):
        # กรณีทั่วไปที่ไม่ใช่ Funny
        self.assertEqual(funnyString("bcxz"), "Not Funny")

    def test_palindrome_funny(self):
        # กรณีเป็น Palindrome ที่ต้องเป็น Funny เสมอ
        self.assertEqual(funnyString("abba"), "Funny")

    def test_all_same_characters(self):
        # กรณีที่มีตัวอักษรเดียวกันทั้งหมด (Funny เสมอ)
        self.assertEqual(funnyString("aaaa"), "Funny")

    def test_large_input_funny(self):
        # กรณี input ที่ยาวและเป็น Funny
        self.assertEqual(funnyString("abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcba"), "Funny")

    def test_large_input_not_funny(self):
        # กรณี input ที่ยาวและไม่ใช่ Funny
        self.assertEqual(funnyString("abcdefghijklmnopqrstuvwxyzzyxwvutsrqponmlkjihgfedcbx"), "Not Funny")

