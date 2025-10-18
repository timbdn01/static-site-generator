import os
import shutil
import sys
from generate_page import generate_pages_recursive

basepath = "./"
if len(sys.argv) > 1 and sys.argv[1] != "":
    basepath = sys.argv[1]
dir_path_static = "./static"
dir_path_docs = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_docs):
        shutil.rmtree(dir_path_docs)
    # If a basepath is provided like '/static-site-generator/', we should
    # write the generated site and static files into `public/<basepath>` so
    # that requests to '/static-site-generator/...' resolve when serving
    # the `public` directory as the server root.
    dest_public_root = dir_path_docs
    if basepath != "./" and basepath.startswith("/"):
        sub = basepath.strip("/")
        if sub != "":
            dest_docs_root = os.path.join(dir_path_docs, sub)

    # Ensure the destination root exists before copying
    os.makedirs(dest_docs_root, exist_ok=True)

    print("Copying static files to public directory...")
    static_to_public(dir_path_static, dest_public_root)

    print("Generating page...")
    generate_pages_recursive(
        dir_path_content,
        template_path,
        dest_public_root,
        basepath,
    )


def static_to_public(source_dir="static", dest_dir="public"):
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    for filename in os.listdir(source_dir):
        from_path = os.path.join(source_dir, filename)
        dest_path = os.path.join(dest_dir, filename)
        print(f" * {from_path} -> {dest_path}")
        if os.path.isfile(from_path):
            shutil.copy(from_path, dest_path)
        else:
            static_to_public(from_path, dest_path)
    

main()