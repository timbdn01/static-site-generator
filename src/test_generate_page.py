from generate_page import generate_page
import unittest
import os

class TestGeneratePage(unittest.TestCase):
    def test_case(self):
        generate_page("content/index.md", "template.html", "public/index.html")
        self.assertTrue(os.path.exists("public/index.html"))
        with open("public/index.html", "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn("<h1>Welcome to My Static Site</h1>", content)
            self.assertIn("<p>This is a sample paragraph in my static site.</p>", content)