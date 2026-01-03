from enum import Enum
from textnode_utils import markdown_to_blocks, text_to_textnodes, text_node_to_html_node
from htmlnode import ParentNode, LeafNode


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"
    CODE = "code"


def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.ULIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.OLIST
    return BlockType.PARAGRAPH


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    return [text_node_to_html_node(node) for node in text_nodes]


def markdown_to_html_node(md):
    blocks = markdown_to_blocks(md)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            num_of_hashes = len(block.split(" ")[0])
            text = block[num_of_hashes + 1 :]
            children.append(ParentNode(f"h{num_of_hashes}", text_to_children(text)))

        elif block_type == BlockType.PARAGRAPH:
            children.append(ParentNode("p", text_to_children(block)))

        elif block_type == BlockType.QUOTE:
            quoted = "\n".join(line[1:].lstrip() for line in block.split("\n"))
            children.append(ParentNode("blockquote", text_to_children(quoted)))

        elif block_type == BlockType.UNORDERED_LIST:
            items = []
            for line in block.split("\n"):
                items.append(ParentNode("li", text_to_children(line[2:].lstrip())))

            children.append(ParentNode("ul", text_to_children(items)))

        elif block_type == BlockType.ORDERED_LIST:
            items = []
            for line in block.split("\n"):
                items.append(ParentNode("li", text_to_children(line[2:].lstrip())))

            children.append(ParentNode("ol", text_to_children(items)))

        elif block_type == BlockType.CODE:
            code_text = block[3:-3].strip()
            code_node = LeafNode(None, code_text)
            children.append(ParentNode("pre", [ParentNode("code"), [code_node]]))

        else:
            raise ValueError(f"Unknown block type: {block_type}")

    return ParentNode("div", children)
