import unittest
from Two_Characters import alternate  # เปลี่ยน 'your_module' เป็นชื่อไฟล์ที่มีฟังก์ชัน alternate

class TestAlternate(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(alternate(""), 0)  # ทดสอบสตริงว่าง

    def test_single_char(self):
        self.assertEqual(alternate("a"), 0)  # ทดสอบสตริงที่มีตัวอักษรเดียว

    def test_two_chars(self):
        self.assertEqual(alternate("ab"), 2)  # ทดสอบสตริงที่มีตัวอักษร 2 ตัวสลับกัน

    def test_valid_alternate(self):
        self.assertEqual(alternate("ababab"), 6)  # ทดสอบสตริงที่สลับกันอย่างถูกต้อง

    def test_invalid_alternate(self):
        self.assertEqual(alternate("aabba"), 0)  # ทดสอบสตริงที่สลับกันไม่ถูกต้อง

    def test_mixed_chars(self):
        self.assertEqual(alternate("abcabc"), 4)  # ทดสอบสตริงที่มีตัวอักษรผสมและมีสตริงย่อยที่ถูกต้อง

    def test_large_string(self):
        self.assertEqual(alternate("abacabadabacaba"), 3)  # ทดสอบสตริงขนาดใหญ่ที่มีสตริงย่อยที่ถูกต้อง

    def test_all_same_char(self):
        self.assertEqual(alternate("aaaaa"), 0)  # ทดสอบสตริงที่มีตัวอักษรซ้ำทั้งหมด

    def test_no_alternate(self):
        self.assertEqual(alternate("abcde"), 2)  # ทดสอบสตริงที่ไม่มีสตริงย่อยที่สลับกันถูกต้อง

    def test_complex_case(self):
        self.assertEqual(alternate("beabeefeab"), 5)  # ทดสอบกรณีที่ซับซ้อนที่มีสตริงย่อยที่ถูกต้อง

