def test_should_read_csv(
    tmp_path
):
    csv_file = (
        tmp_path / "test.csv"
    )

    csv_file.write_text(
        "name,age\njohn,30"
    )

    service = ExcelService()

    dataframe = service.read_csv(
        csv_file
    )

    assert len(dataframe) == 1