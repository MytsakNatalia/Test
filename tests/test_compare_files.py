import pytest
import os
from main import  compare_files, read_file
@pytest.fixture
def create_input_files():
    file1_path = "file1.txt"
    file2_path = "file2.txt"
    with open(file1_path, "w") as file1:
        file1.write("line1\nline2\n")
    with open(file2_path, "w") as file2:
        file2.write("line2\nline3\n")
    return file1_path, file2_path

def test_compare_files(create_input_files):
    file1_path, file2_path = create_input_files
    compare_files(file1_path, file2_path)
    same_path = "same.txt"
    diff_path = "diff.txt"
    assert os.path.exists(same_path)  # Check if same.txt was generated
    assert os.path.exists(diff_path)  # Check if diff.txt was generated

    with open(same_path, "r") as same_file:
        same_lines = same_file.readlines()
    with open(diff_path, "r") as diff_file:
        diff_lines = diff_file.readlines()

    # Sort lines to make order irrelevant
    same_lines.sort()
    diff_lines.sort()

    # Compare sorted lines
    assert same_lines == ["line2\n"]
    assert diff_lines == ["line1\n", "line3\n"]


