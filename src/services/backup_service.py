from datetime import datetime
from pathlib import Path
import shutil

from src.interfaces.service import Service


class BackupService(Service):

    def create_backup(
        self,
        source_file: Path,
        backup_directory: Path
    ) -> Path:

        backup_directory.mkdir(
            parents=True,
            exist_ok=True
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        backup_path = (
            backup_directory /
            f"{timestamp}_{source_file.name}"
        )

        shutil.copy2(
            source_file,
            backup_path
        )

        return backup_path