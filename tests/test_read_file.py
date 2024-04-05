import  pytest
from main import  read_file
@pytest.fixture
def file_content():
    return "line1\nline2\nline3"

@pytest.fixture
def create_test_file(tmp_path, file_content):
    file_path = tmp_path / "test_file.txt"
    with open(file_path, "w") as file:
        file.write(file_content)
    return file_path


def test_read_file(create_test_file, file_content):
    file_path = create_test_file
    lines = read_file(file_path)
    processed_lines = {line.strip() for line in lines}

    # Process expected lines to match the format of lines read from the file
    expected_lines = {line for line in file_content.strip().split('\n')}

    assert processed_lines == expected_lines
