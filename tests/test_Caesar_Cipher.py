import unittest
from Caesar_Cipher import caesarCipher  # เปลี่ยน 'your_module' เป็นชื่อไฟล์ที่มีฟังก์ชัน caesarCipher

class TestCaesarCipher(unittest.TestCase):

    def test_lowercase_shift(self):
        # กรณีตัวอักษรพิมพ์เล็ก
        self.assertEqual(caesarCipher("abc", 3), "def")

    def test_uppercase_shift(self):
        # กรณีตัวอักษรพิมพ์ใหญ่
        self.assertEqual(caesarCipher("XYZ", 3), "ABC")

    def test_mixed_case(self):
        # กรณีผสมตัวพิมพ์เล็กและใหญ่
        self.assertEqual(caesarCipher("AbC", 1), "BcD")

    def test_non_alpha_characters(self):
        # กรณีมีอักขระพิเศษและช่องว่าง (ไม่เปลี่ยนแปลง)
        self.assertEqual(caesarCipher("Hello, World!", 5), "Mjqqt, Btwqi!")

    def test_large_shift(self):
        # กรณีค่า k ที่มากกว่า 26
        self.assertEqual(caesarCipher("xyz", 29), "abc")

    def test_no_shift(self):
        # กรณีไม่เลื่อน (k = 0)
        self.assertEqual(caesarCipher("abc", 0), "abc")

    def test_full_rotation(self):
        # กรณีหมุนครบรอบ (k = 26)
        self.assertEqual(caesarCipher("abc", 26), "abc")

    def test_empty_string(self):
        # กรณี input ว่าง
        self.assertEqual(caesarCipher("", 5), "")

    def test_large_input(self):
        # กรณีข้อความยาว
        self.assertEqual(caesarCipher("a" * 1000, 1), "b" * 1000)

    def test_negative_shift(self):
        # กรณีค่า k ติดลบ (ควรเลื่อนย้อนกลับ)
        self.assertEqual(caesarCipher("abc", -3), "xyz")
