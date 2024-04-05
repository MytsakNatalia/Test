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

    # Read the content of the generated files and assert their content
    with open(same_path, "r") as same_file:
        assert same_file.read() == "line2\n"
    with open(diff_path, "r") as diff_file:
        assert diff_file.read() == "line3\nline1\n"