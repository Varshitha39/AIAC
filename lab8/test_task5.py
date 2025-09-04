import unittest
from datetime import datetime

def valid_date(date_str):
    # Example implementation, replace with your actual function
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

class TestValidDate(unittest.TestCase):
    def test_valid_date(self):
        self.assertTrue(valid_date("2024-06-01"))
        self.assertTrue(valid_date("2000-01-01"))
        self.assertFalse(valid_date("2024-13-01"))  # Invalid month
        self.assertFalse(valid_date("not-a-date"))
        self.assertFalse(valid_date("2024-02-30"))  # Invalid day

if __name__ == "__main__":
    unittest.main()