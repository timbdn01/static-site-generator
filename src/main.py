from textnode import TextNode, TextType

def main():
    node = TextNode("This is some anchor text", text_type=TextType.LINK, url = "https://www.boot.dev")
    print(node.__repr__())

main()