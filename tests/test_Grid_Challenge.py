import unittest
from Grid_Challenge import gridChallenge  # เปลี่ยน 'your_module' เป็นชื่อไฟล์ที่มีฟังก์ชัน gridChallenge

class TestGridChallenge(unittest.TestCase):

    def test_sorted_grid(self):
        # กรณีที่ grid ถูกจัดเรียงอยู่แล้ว
        grid = ["abc", "bcd", "cde"]
        self.assertEqual(gridChallenge(grid), 'YES')

    def test_valid_grid_no(self):
        grid = [
            'abc',
            'def',
            'cba'
        ]
        self.assertEqual(gridChallenge(grid), "NO")

    def test_single_row(self):
        # กรณีที่มีเพียงแถวเดียว
        grid = ["zxc"]
        self.assertEqual(gridChallenge(grid), 'YES')

    def test_single_column(self):
        # กรณีที่มีคอลัมน์เดียว
        grid = ["a", "b", "c"]
        self.assertEqual(gridChallenge(grid), 'YES')

    def test_empty_grid(self):
        # กรณีที่ grid ว่าง
        grid = []
        self.assertEqual(gridChallenge(grid), 'NO')

    def test_identical_rows(self):
        # กรณีที่ทุกแถวเหมือนกัน
        grid = ["xxx", "xxx", "xxx"]
        self.assertEqual(gridChallenge(grid), 'YES')

    def test_reverse_sorted_grid(self):
        # กรณีที่ grid เรียงจากมากไปน้อยในแนวนอน
        grid = ["cba", "fed", "ihg"]
        self.assertEqual(gridChallenge(grid), 'YES')

    def test_large_grid_yes(self):
        # กรณีที่มี grid ขนาดใหญ่และสามารถจัดเรียงได้
        grid = ["abcdefg", "bcdefgh", "cdefghi", "defghij"]
        self.assertEqual(gridChallenge(grid), 'YES')

    def test_large_grid_no(self):
        # กรณีที่มี grid ขนาดใหญ่และไม่สามารถจัดเรียงได้
        grid = ["abcdefg", "bcdefgh", "cdefghi", "aaaaaa"]
        self.assertEqual(gridChallenge(grid), 'NO')
    def test_len_every_row(self):
        # กรณีที่มีความยาวของแต่ละแถวไม่เท่ากัน
        grid = ["abc", "abcd", "abcde"]
        self.assertEqual(gridChallenge(grid), 'NO')