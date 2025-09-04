import unittest
from task1 import is_valid_email  # Import the function to test

class TestEmailValidation(unittest.TestCase):
    def test_valid_emails(self):
        valid_emails = [
            "user@example.com",
            "john.doe-123@example-domain.com",
            "a_b.c-d@sub.domain.com",
            "a@b.co",
            "abc.def@ghi.jkl.mno"
        ]
        for email in valid_emails:
            with self.subTest(email=email):
                self.assertTrue(is_valid_email(email))

    def test_invalid_emails(self):
        invalid_emails = [
            "userexample.com",         # no @
            "user@@example.com",       # multiple @
            ".user@example.com",       # starts with special char
            "user.@example.com",       # ends with special char
            "user@.example.com",       # domain starts with special char
            "user@example.com.",       # domain ends with special char
            "user@domaincom",          # no dot in domain
            "user@domain..com",        # consecutive dots
            "user@-domain.com",        # domain starts with hyphen
            "user@domain-.com",        # domain ends with hyphen
            "user@domain@com",         # multiple @
            "user@domain",             # no dot in domain
            "user@.com",               # domain starts with dot
            "user@com.",               # domain ends with dot
        ]
        for email in invalid_emails:
            with self.subTest(email=email):
                self.assertFalse(is_valid_email(email))

if __name__ == "__main__":
    unittest.main()