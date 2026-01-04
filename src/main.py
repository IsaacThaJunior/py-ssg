from recursive_file_copier import (
    recursive_file_copier,
    generate_pages_recursive,
)


def main():
    recursive_file_copier("static", "public")
    generate_pages_recursive("content", "template.html", "public")


main()
