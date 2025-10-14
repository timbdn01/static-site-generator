import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextNode, TextType

class TestHtmlNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", [], [], {"href": "https://example.com"})
        node2 = HTMLNode("a",[], [], {"href": "https://anotherexample.com"})
        node3 = HTMLNode("div", props={"class": "container"})
        self.assertEqual(node.props_to_html(), ' href="https://example.com"')
        self.assertNotEqual(node2.props_to_html(), ' href="https://example.com"')
        self.assertEqual(node3.props_to_html(), ' class="container"')

    def test_leaf_to_html(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        node2 = LeafNode(None, "Just some text")
        self.assertEqual(node2.to_html(), "Just some text")
        node3 = LeafNode("img", "Image", props={"src": "image.png", "alt": "An image"})
        self.assertEqual(node3.to_html(), '<img src="image.png" alt="An image">Image</img>')
        with self.assertRaises(ValueError):
            node4 = LeafNode("p", None)
            node4.to_html()

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        child_node2 = LeafNode("span", "child2")
        child_node3 = LeafNode("span", "child3")
        parent_node = ParentNode("div", [child_node, child_node2, child_node3])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span><span>child2</span><span>child3</span></div>")


    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    def test_parent_to_html_errors(self):
        with self.assertRaises(ValueError):
            node = ParentNode(None, [LeafNode("span", "child")])
            node.to_html()
        with self.assertRaises(ValueError):
            node = ParentNode("div", [])
            node.to_html()
    def test_parent_to_html_with_props(self):
        child_node = LeafNode("span", "child", props={"class": "text"})
        parent_node = ParentNode("div", [child_node], props={"id": "main"})
        self.assertEqual(
            parent_node.to_html(),
            '<div id="main"><span class="text">child</span></div>',
        )
    def test_to_html_with_grandchildren_and_props(self):
        grandchild_node = LeafNode("b", "grandchild", props={"style": "font-weight:bold;"})
        child_node = ParentNode("span", [grandchild_node], props={"class": "highlight"})
        parent_node = ParentNode("div", [child_node], props={"id": "container"})
        self.assertEqual(
            parent_node.to_html(),
            '<div id="container"><span class="highlight"><b style="font-weight:bold;">grandchild</b></span></div>',
        )
    
    def test_text(self):
        node = TextNode("This is a text node", TextType.PLAIN)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)
        self.assertEqual(html_node.value, "This is a text node")
        node2 = TextNode("This is bold Text", TextType.BOLD)
        html_node2 = text_node_to_html_node(node2)
        self.assertEqual(html_node2.tag, "b")
        self.assertEqual(html_node2.value, "This is bold Text")
        


    