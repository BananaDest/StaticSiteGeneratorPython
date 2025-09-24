import unittest
from splitnodes import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNodes(unittest.TestCase):
    def test_code(self):
        new_nodes_correct = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, new_nodes_correct)

    def test_bold(self):
        new_nodes_correct = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, new_nodes_correct)

    def test_italic(self):
        new_nodes_correct = [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, new_nodes_correct)

    def test_multiple_delimiter(self):
        new_nodes_correct = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("two", TextType.ITALIC),
            TextNode(" ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" words.", TextType.TEXT),
        ]
        node = TextNode("This is text with _two_ _italic_ words.", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, new_nodes_correct)

    def test_all(self):
        new_nodes_correct = [
            TextNode("an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word, a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word, and a ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" word.", TextType.TEXT),
        ]
        node = TextNode(
            "an _italic_ word, a **bold** word, and a `code` word.",
            TextType.TEXT,
        )
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        new_nodes = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
        self.assertEqual(new_nodes, new_nodes_correct)

    def test_error(self):
        node = TextNode("This is text with an _italic word", TextType.TEXT)
        with self.assertRaises(Exception) as exc:
            split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(str(exc.exception), "No closing delimiter.")


if __name__ == "__main__":
    unittest.main()
