#!/usr/bin/env python3
import unittest
from user_validations import validate_user

class TestValidateUser(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_user('valid'),True)
    
    def test_too_short(self):
        self.assertEqual(validate_user('it'),False)

    def test_invalid_characters(self):
        self.assertEqual(validate_user('11'),False)
    

unittest.main()
