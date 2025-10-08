import os
import shutil
from generate_page import generate_pages_recursively
import sys


def main():
    basepath = sys.argv[1]
    if os.path.exists("public/"):
        shutil.rmtree("public/")
    copy_recursively("static/", "public/")
    generate_pages_recursively("content/", "template.html", "public/")


def copy_recursively(src, dest):
    # try catch was just to see error messages
    # try:
    #     print(f"source: {src}")
    #     print(f"destination: {dest}")
    # not needed, normal path works
    #     src_abs = os.path.abspath(os.path.join("./", src))
    #     dest_abs = os.path.abspath(os.path.join("./", dest))
    # isfile technically will catch this error
    #     if not os.path.exists(src_abs):
    #         raise ValueError("source path does not exist")
    # adding this breaks it
    #     if os.path.exists(dest):
    #         shutil.rmtree(dest)
    # this is basically the same, mine adds more recursion steps as it creates each file individually
    #     if os.path.isfile(src_abs):
    #         shutil.copy(src_abs, dest_abs)
    #         return
    #     else:
    #         os.mkdir(dest)
    #         for entry in os.listdir(src):
    #             new_dest = os.path.join(dest_abs, entry)
    #             new_src = os.path.join(src_abs, entry)
    #             copyContents(new_src, new_dest)
    # except Exception as e:
    #     raise e
    if not os.path.exists(dest):
        os.mkdir(dest)
    for entry in os.listdir(src):
        src_path = os.path.join(src, entry)
        dest_path = os.path.join(dest, entry)
        print(f" * {src_path} -> {dest_path}")
        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_path)
        else:
            copy_recursively(src_path, dest_path)


main()
