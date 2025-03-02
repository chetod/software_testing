import unittest
from Alternating_Characters import alternatingCharacters  

class TestAlternatingCharacters(unittest.TestCase):
    
    def test_basic_nodel(self):
        # กรณีไม่มีอักขระซ้ำติดกัน
        self.assertEqual(alternatingCharacters("ABABAB"), 0)

    def test_all_repeatchar(self):
        # กรณีมีอักขระเดียวกันทั้งหมด
        self.assertEqual(alternatingCharacters("AAAA"), 3)

    def test_someduplicate(self):
        # กรณีที่มีอักขระสลับกันและมีซ้ำบางส่วน
        self.assertEqual(alternatingCharacters("AABBAABB"), 4)

    def test_one_char(self):
        # กรณีมีอักขระเดียว
        self.assertEqual(alternatingCharacters("A"), 0)

    def test_two_different_characters(self):
        # กรณีมี 2 ตัวอักษรที่แตกต่างกัน
        self.assertEqual(alternatingCharacters("AB"), 0)

    def test_two_same_characters(self):
        # กรณีมี 2 ตัวอักษรที่เหมือนกัน
        self.assertEqual(alternatingCharacters("AA"), 1)

    def test_long_string_with_duplicates(self):
        # กรณีข้อความยาวที่มีการซ้ำกัน
        self.assertEqual(alternatingCharacters("AABBAABBAABBAA"), 7)

    def test_empty_string(self):
        # กรณี input ว่าง
        self.assertEqual(alternatingCharacters(""), 0)

    def test_alternating_large_input(self):
        # กรณีข้อความยาวที่ไม่มีการซ้ำกัน
        self.assertEqual(alternatingCharacters("AB" * 10), 0)

