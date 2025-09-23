import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props(self):
        node = HTMLNode(
            None,
            None,
            None,
            {
                "href": "https://www.google.com",
                "target": "_blank",
            },
        )
        props = node.props_to_html()
        self.assertEqual(props, ' href="https://www.google.com" target="_blank"')

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    def test_no_props(self):
        node = HTMLNode(
            None,
            None,
            None,
            None,
        )
        with self.assertRaises(Exception):
            node.props_to_html()


if __name__ == "__main__":
    unittest.main()
