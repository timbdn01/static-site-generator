from textnode import TextNode, TextType

class HTMLNode:
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    def to_html(self):
        raise NotImplementedError("Subclasses should implement this method")

    def props_to_html(self):
        props_str = ""
        for key, value in self.props.items():
            props_str += f' {key}="{value}"'
        return props_str

    def __repr__(self):
        return f"HTMLNode(tag={self.tag}, value={self.value}, children={self.children}, props={self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None):
        super().__init__(tag=tag, value=value, props=props)
    def to_html(self):
        if not self.value:
            raise ValueError("LeafNode must have a value")
        elif not self.tag:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict = None):
        super().__init__(tag=tag, children=children, props=props)
    def to_html(self):
        if not self.tag:
            raise ValueError("ParentNode must have a tag")
        if not self.children:
            raise ValueError("ParentNode must have children")
        return f"<{self.tag}{self.props_to_html()}>" + "".join(child.to_html() for child in self.children) + f"</{self.tag}>"
    
def text_node_to_html_node(text_node: TextNode) -> HTMLNode:
    if text_node.text_type == TextType.PLAIN:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == TextType.LINK:
        if not text_node.url:
            raise ValueError("Link TextNode must have a URL")
        return LeafNode("a", text_node.text, props={"href": text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        if not text_node.url:
            raise ValueError("Image TextNode must have a URL")
        return LeafNode("img", text_node.text, props={"src": text_node.url, "alt": text_node.text})
    else:
        raise ValueError("Unknown TextType")