from block_markdown import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node
import unittest

class TestBlockMarkdown(unittest.TestCase):
        def test_markdown_to_blocks(self):
            md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
            blocks = markdown_to_blocks(md)
            self.assertEqual(
                blocks,
                [
                    "This is **bolded** paragraph",
                    "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                    "- This is a list\n- with items",
                ],
        )
        def test_block_to_block_type(self):
            self.assertEqual(block_to_block_type("# Heading 1"), BlockType.HEADING)
            self.assertEqual(
                block_to_block_type("```python\nprint('Hello, world!')\n```"),
                BlockType.CODE,
            )
            self.assertEqual(block_to_block_type("> This is a quote"), BlockType.QUOTE)
            self.assertEqual(
                block_to_block_type("- This is an unordered list item"),
                BlockType.ULIST,
            )
            self.assertEqual(
                block_to_block_type("1. This is an ordered list item"),
                BlockType.OLIST,
            )
            self.assertEqual(
                block_to_block_type("This is a regular paragraph."),
                BlockType.PARAGRAPH,
            )

        def test_paragraphs(self):
            md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(
                html,
                "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
            )

        def test_codeblock(self):
            md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

            node = markdown_to_html_node(md)
            html = node.to_html()
            self.assertEqual(
                html,
                "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
            )