from textnode import TextNode, TextType
from extractmarkdownlinks import extract_markdown_links, extract_markdown_images


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


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        images = extract_markdown_images(original_text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            sections = original_text.split(f"![{image[0]}]({image[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        original_text = old_node.text
        links = extract_markdown_links(original_text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            sections = original_text.split(f"[{link[0]}]({link[1]})", 1)
            if len(sections) != 2:
                raise ValueError("invalid markdown, link section not closed")
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            original_text = sections[1]
        if original_text != "":
            new_nodes.append(TextNode(original_text, TextType.TEXT))
    return new_nodes


def text_to_textnodes(text):
    textNode = TextNode(text, TextType.TEXT)
    bolds = split_nodes_delimiter([textNode], "**", TextType.BOLD)
    italics = split_nodes_delimiter(bolds, "_", TextType.ITALIC)
    codeblocks = split_nodes_delimiter(italics, "`", TextType.CODE)
    images = split_nodes_image(codeblocks)
    return split_nodes_link(images)
