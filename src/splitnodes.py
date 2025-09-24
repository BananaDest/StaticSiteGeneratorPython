from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        parts = node.text.split(delimiter)
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if len(parts) % 2 == 0:
            raise Exception("No closing delimiter.")
        list = [
            TextNode(part, TextType.TEXT) if i % 2 == 0 else TextNode(part, text_type)
            for i, part in enumerate(parts)
        ]
        new_nodes.extend(list)
    return new_nodes
