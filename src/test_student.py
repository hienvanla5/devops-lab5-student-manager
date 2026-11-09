import unittest

from student import Student

class TestStudentAge(unittest.TestCase):
  def test_valid_age(self):
    self.assertTrue(
      Student("SV001", "Nguyen Van A", 20, "K20").is_valid_age()
    )

  def test_invalid_age(self):
    self.assertFalse(
      Student("SV002", "Tran Thi B", 15, "K20").is_valid_age()
    )

if __name__ == "__main__":
  unittest.main()