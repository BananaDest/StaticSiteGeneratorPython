import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("This is another text node", TextType.IMAGE)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_neq_url(self):
        node = TextNode("This is a text node", TextType.BOLD, "boot.dev")
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")

    def test_BOLD(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "b")
        self.assertEqual(html_node.value, "This is a bold node")

    def test_ITALIC(self):
        node = TextNode("This is an italic node", TextType.ITALIC)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "i")
        self.assertEqual(html_node.value, "This is an italic node")

    def test_CODE(self):
        node = TextNode("This is a code node", TextType.CODE)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "code")
        self.assertEqual(html_node.value, "This is a code node")

    def test_LINK(self):
        node = TextNode("This is a link node", TextType.LINK)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.value, "This is a link node")

    def test_IMAGE(self):
        node = TextNode("This is an image node", TextType.IMAGE, "boot.dev")
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(
            html_node.props, {"src": "boot.dev", "alt": "This is an image node"}
        )

    def test_INVALID(self):
        node = TextNode("This is an invalid node", "INVALID")
        with self.assertRaises(ValueError) as exc:
            text_node_to_html_node(node)
        self.assertEqual(str(exc.exception), "invalid text type: INVALID")


if __name__ == "__main__":
    unittest.main()
