import os
import shutil

from blocknode import markdown_to_html_node
from textnode_utils import extract_title


def recursive_file_copier(src, dst):
    # Check if destination exists and delete it
    if os.path.exists(dst):
        shutil.rmtree(dst)
    # Then creates the destination again
    os.mkdir(dst)

    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)
        if os.path.isdir(src_path):
            print(f"Creating Directory: {dst_path}")
            recursive_file_copier(src_path, dst_path)
        else:
            print(f"Copying file: {src_path} -> {dst_path}")
            shutil.copyfile(src_path, dst_path)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path}")

    with open(from_path, "r", encoding="utf-8") as f:
        markdown_content = f.read()

    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()

    title = extract_title(markdown_content)

    final_html = template_content.replace("{{ Title }}", title).replace(
        "{{ Content }}", html_content
    )

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(final_html)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # if os.path.exists(dest_dir_path):
    #     shutil.rmtree(dest_dir_path)
    # os.mkdir(dest_dir_path)

    for item in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content, item)
        dst_path = os.path.join(dest_dir_path, item)
        if os.path.isdir(src_path):
            print(f"Creating Directory: {dst_path}")
            generate_pages_recursive(src_path, template_path, dst_path)
        else:
            name, ext = os.path.splitext(item)
            new_name = f"{name}.html"
            dst_path = os.path.join(dest_dir_path, new_name)
            print(f"Generating page from {src_path} to {dst_path}")
            generate_page(src_path, template_path, dst_path)
