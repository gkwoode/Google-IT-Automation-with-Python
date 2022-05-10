from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basic(self):
        testcase = "Woode, Godwin"
        expected = "Godwin Woode"
        self.assertEqual(rearrange_name(testcase), expected)

    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(rearrange_name(testcase), expected)

    def test_double_name(self):
        testcase = "Woode, Godwin K."
        expected = "Godwin K. Woode"
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main()