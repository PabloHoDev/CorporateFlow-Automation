def test_should_list_files(
    tmp_path
):
    file = tmp_path / "teste.xlsx"

    file.touch()

    service = FileService()

    files = service.list_files(
        tmp_path
    )

    assert len(files) == 1