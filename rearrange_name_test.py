from advance_regex import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_two_names(self):
        testcase = 'Barack, Obama'
        expected = 'Obama Barack'
        self.assertEqual(rearrange_name(testcase),expected)

    def test_empty(self):
        testcase = ''
        expected = ''
        self.assertEqual(rearrange_name(testcase),expected)

    def test_more_names(self):
        testcase = 'Mark, Paul M.'
        expected = 'Paul M. Mark'
        self.assertCountEqual(rearrange_name(testcase),expected)

    def test_one_name(self):
        testcase = 'Elizabeth'
        expected = 'Elizabeth'
        self.assertEqual(rearrange_name(testcase),expected)

unittest.main()