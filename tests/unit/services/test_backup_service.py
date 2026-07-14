def test_should_create_backup(
    tmp_path
):
    source = tmp_path / "arquivo.xlsx"

    source.touch()

    backup_folder = (
        tmp_path / "backup"
    )

    backup_folder.mkdir()

    service = BackupService()

    backup_file = service.create_backup(
        source,
        backup_folder
    )

    assert backup_file.exists()