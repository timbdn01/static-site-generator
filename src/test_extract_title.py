from extract_title import extract_title
import unittest

class TestExtractTitle(unittest.TestCase):
    def test_extract_title_success(self):
        md = """# This is the Title"""
        title = extract_title(md)
        self.assertEqual(title, "This is the Title")

    def test_extract_title_with_leading_whitespace(self):
        md = """   # Leading Whitespace Title"""
        title = extract_title(md)
        self.assertEqual(title, "Leading Whitespace Title")

    def test_extract_title_no_title(self):
        md = """This markdown has no title."""
        with self.assertRaises(ValueError):
            extract_title(md)
    
    def test_extract_title_multiple_lines(self):
        md = """Some introduction text.
# Actual Title Here
More text."""
        title = extract_title(md)
        self.assertEqual(title, "Actual Title Here")

    def test_extract_title_empty_markdown(self):
        md = """"""
        with self.assertRaises(ValueError):
            extract_title(md)