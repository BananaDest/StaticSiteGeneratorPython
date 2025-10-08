import os
from markdown_blocks import markdown_to_html_node
from extract_title import extract_title


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_file = ""
    with open(from_path) as file:
        from_file = file.read()
    with open(template_path) as file:
        template_file = file.read()
    from_html_node = markdown_to_html_node(from_file)
    from_html_string = from_html_node.to_html()
    title = extract_title(from_file).split("\n")[0]
    template_full = (
        template_file.replace("{{ Title }}", title)
        .replace("{{ Content }}", from_html_string)
        .replace('href="/', f'href="{basepath}')
        .replace('src="/', f'src="{basepath}')
    )
    with open(dest_path, "w") as file:
        file.write(template_full)


def generate_pages_recursively(
    dir_path_content, template_path, dest_dir_path, basepath
):
    for entry in os.listdir(dir_path_content):
        if os.path.isfile(os.path.join(dir_path_content, entry)):
            generate_page(
                os.path.join(dir_path_content, entry),
                template_path,
                os.path.join(dest_dir_path, entry.replace(".md", ".html")),
                basepath,
            )
        else:
            os.makedirs(os.path.join(dest_dir_path, entry), exist_ok=True)
            generate_pages_recursively(
                os.path.join(dir_path_content, entry),
                template_path,
                os.path.join(dest_dir_path, entry),
                basepath,
            )
