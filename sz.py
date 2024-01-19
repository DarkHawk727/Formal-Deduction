import os
from tabulate import tabulate


def count_file_details(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        num_lines = content.count("\n") + 1
        num_chars = len(content)
        return num_lines, num_chars


def count_lines_chars_in_directory(directory_path):
    file_details = []
    total_lines = total_chars = 0
    for root, _, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".py") and file != "sz.py":
                file_path = os.path.join(root, file)
                num_lines, num_chars = count_file_details(file_path)
                total_lines += num_lines
                total_chars += num_chars
                relative_path = os.path.relpath(file_path, directory_path)
                file_details.append((relative_path, num_lines, num_chars))
    return file_details, total_lines, total_chars


directory = (
    "C:/Users/Arjun Sarao/Formal-Deduction"  # Replace with your project directory path
)
file_details, total_lines, total_chars = count_lines_chars_in_directory(directory)


file_details.append(
    (
        "\033[1mTotal:\033[0m",
        "\033[1m" + str(total_lines) + "\033[0m",
        "\033[1m" + str(total_chars) + "\033[0m",
    )
)  # Append total counts
headers = ["File", "Lines", "Characters"]
table = tabulate(file_details, headers=headers, tablefmt="simple")
print(table)
