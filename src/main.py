from recursive_file_copier import (
    recursive_file_copier,
    generate_pages_recursive,
)
import sys


def main():
    basepath = sys.argv[1] if len(sys.argv) > 1 else "/"

    recursive_file_copier("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)


main()
