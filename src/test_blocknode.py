import unittest

from blocknode import markdown_to_html_node
from textnode_utils import extract_title


class TestBlockNode(unittest.TestCase):
    def test_markdown_paragraph(self):
        md = "Hello **world**"
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(), "<div><p>Hello <b>world</b></p></div>")

    def test_markdown_heading(self):
        md = "# Hello"
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(), "<div><h1>Hello</h1></div>")

    def test_markdown_code_block(self):
        md = "```print('hi')```"
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(), "<div><pre><code>print('hi')</code></pre></div>"
        )

    def test_markdown_list(self):
        md = "- one\n- two"
        node = markdown_to_html_node(md)
        self.assertEqual(node.to_html(), "<div><ul><li>one</li><li>two</li></ul></div>")

    def test_markdown_quote(self):
        md = "> hello world"
        node = markdown_to_html_node(md)
        self.assertEqual(
            node.to_html(), "<div><blockquote>hello world</blockquote></div>"
        )
        
    def test_simple_h1(self):
        md = "# Hello"
        self.assertEqual(extract_title(md), "Hello")

    def test_h1_with_whitespace(self):
        md = "   #    My Title   "
        self.assertEqual(extract_title(md), "My Title")

    def test_h1_not_first_line(self):
        md = "Some intro\n# Header Line\nMore text"
        self.assertEqual(extract_title(md), "Header Line")

    def test_multiple_h1s(self):
        md = "# First Title\n# Second Title"
        self.assertEqual(extract_title(md), "First Title")  # should return the first h1

    def test_no_h1(self):
        md = "## Subtitle\nSome paragraph"
        with self.assertRaises(Exception):
            extract_title(md)

    def test_h2_should_not_count(self):
        md = "## Not H1"
        with self.assertRaises(Exception):
            extract_title(md)
