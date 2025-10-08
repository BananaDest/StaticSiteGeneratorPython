import unittest

from extract_title import extract_title


class testExtractTitle(unittest.TestCase):
    def test_extract_title(self):
        title = extract_title("# Hello")
        self.assertEqual(title, "Hello")

    def test_extract_title_no_title(self):
        with self.assertRaises(ValueError) as exc:
            title = extract_title("132 Hello")
        self.assertEqual(str(exc.exception), "no header")

    def test_extract_title_no_h1(self):
        with self.assertRaises(ValueError) as exc:
            title = extract_title("## Hello")
        self.assertEqual(str(exc.exception), "no header")
