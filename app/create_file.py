import os
import sys
from datetime import datetime


def create_file(file_path):
    content = []
    print("Enter content line:")
    while True:
        line = input()
        if line.lower() == "stop":
            break
        content.append(line)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    content_with_timestamp = [f"{timestamp}\n"]
    for i, line in enumerate(content, start=1):
        content_with_timestamp.append(f"{i} {line}\n")

    mode = "a" if os.path.exists(file_path) else "w"
    with open(file_path, mode) as file:
        file.writelines(content_with_timestamp)


def main():
    if len(sys.argv) < 3:
        print(
            "Usage: python create_file.py "
            "[-d directory_path1 directory_path2 ...] [-f file_name]"
        )
        return

    try:
        directory_index = sys.argv.index("-d")
        file_index = sys.argv.index("-f")
        if directory_index > file_index:
            raise IndexError()

        if "-d" in sys.argv:
            file_index = sys.argv.index("-f")
            directory_path = os.path.join(
                *sys.argv[directory_index + 1 : file_index])
            os.makedirs(directory_path, exist_ok=True)
            print(f"Directory created: {directory_path}")

        if "-f" in sys.argv:
            file_name = sys.argv[file_index + 1]
            if "-d" in sys.argv:
                file_path = os.path.join(directory_path, file_name)
            else:
                file_path = file_name
            create_file(file_path)
            print(f"File created: {file_path}")

    except Exception:
        print(
            "Usage: python create_file.py"
            "[-d directory_path1 directory_path2 ...] [-f file_name]"
        )
        return


if __name__ == "__main__":
    main()
