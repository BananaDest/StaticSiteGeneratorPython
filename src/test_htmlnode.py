import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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
        self.assertEqual(node.props_to_html(), "")

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_a_with_props(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"}).to_html()
        self.assertEqual(node, '<a href="https://www.google.com">Click me!</a>')

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_multiple_children(self):
        children_nodes = [
            LeafNode("span", "child"),
            LeafNode("span", "child"),
            LeafNode("span", "child"),
        ]
        parent_node = ParentNode("div", children_nodes)
        self.assertEqual(
            parent_node.to_html(),
            "<div><span>child</span><span>child</span><span>child</span></div>",
        )

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_multiple_grandchildren(self):
        grandchildren_nodes = [
            LeafNode("b", "grandchild"),
            LeafNode("b", "grandchild"),
            LeafNode("b", "grandchild"),
        ]
        children_nodes = [
            ParentNode("span", grandchildren_nodes),
            LeafNode("b", "grandchild"),
        ]
        parent_node = ParentNode("div", children_nodes)
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b><b>grandchild</b><b>grandchild</b></span><b>grandchild</b></div>",
        )

    def test_to_html_with_no_children(self):
        parent_node = ParentNode("div", None)
        with self.assertRaises(ValueError) as exc:
            parent_node.to_html()
        self.assertEqual(str(exc.exception), "Children are missing")


if __name__ == "__main__":
    unittest.main()
