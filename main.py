
def read_file(file_name):
    with open(file_name, 'r') as file:
        return set(file.readlines())

def compare_files(file_path1, file_path2):
    # Read file lines
    file1_lines = read_file(file_path1)
    file2_lines = read_file(file_path2)

    # same lines
    same_lines = file1_lines.intersection(file2_lines)

    # different lines
    diff_lines = file1_lines.symmetric_difference(file2_lines)

    # write result
    with open("same.txt", 'w') as same_file:
        same_file.writelines(same_lines)

    with open("diff.txt", 'w') as diff_file:
        diff_file.writelines(diff_lines)

if __name__ == "__main__":
    file1_path = "file1.txt"
    file2_path = "file2.txt"
    with open(file1_path, "w") as file1:
        file1.write("line1\nline2\n")
    with open(file2_path, "w") as file2:
        file2.write("line2\nline3\n")
    compare_files("file1.txt", "file2.txt")