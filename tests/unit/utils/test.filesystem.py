from src.utils.filesystem import FileSystem


def test_should_create_directory(
    tmp_path
):

    directory = (
        tmp_path / "new_folder"
    )

    FileSystem.create_directory(
        directory
    )

    assert directory.exists()


def test_should_detect_existing_file(
    tmp_path
):

    file = tmp_path / "test.txt"

    file.write_text(
        "example"
    )

    assert (
        FileSystem.file_exists(file)
        is True
    )