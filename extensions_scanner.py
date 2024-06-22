import os


def print_file_extensions(directory):
    extensions = set()
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            base_name, extension = os.path.splitext(file_name)
            extensions.add(extension[1:])
    print(extensions)


if __name__ == "__main__":
    directory_path = "images"
    print_file_extensions(directory_path)
