import unittest

from blocknode import markdown_to_html_node

class TestBlockNode(unittest.TestCase):
  def test_markdown_paragraph(self):
    md = "Hello **world**"
    node = markdown_to_html_node(md)
    self.assertEqual(
        node.to_html(),
        "<div><p>Hello <b>world</b></p></div>"
    )


def test_markdown_heading(self):
    md = "# Hello"
    node = markdown_to_html_node(md)
    self.assertEqual(
        node.to_html(),
        "<div><h1>Hello</h1></div>"
    )


def test_markdown_code_block(self):
    md = "```\nprint('hi')\n```"
    node = markdown_to_html_node(md)
    self.assertEqual(
        node.to_html(),
        "<div><pre><code>print('hi')</code></pre></div>"
    )


def test_markdown_list(self):
    md = "- one\n- two"
    node = markdown_to_html_node(md)
    self.assertEqual(
        node.to_html(),
        "<div><ul><li>one</li><li>two</li></ul></div>"
    )


def test_markdown_quote(self):
    md = "> hello\n> world"
    node = markdown_to_html_node(md)
    self.assertEqual(
        node.to_html(),
        "<div><blockquote>hello world</blockquote></div>"
    )

