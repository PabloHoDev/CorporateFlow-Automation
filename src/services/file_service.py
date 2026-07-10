from datetime import datetime
from pathlib import Path

from src.interfaces.service import Service
from src.models.input_file import InputFile


class FileService(Service):

    SUPPORTED_EXTENSIONS = {
        ".xlsx",
        ".xls",
        ".csv"
    }

    def discover_files(
        self,
        input_directory: Path
    ) -> list[InputFile]:

        discovered_files = []

        for path in input_directory.iterdir():

            if not path.is_file():
                continue

            if path.suffix.lower() not in self.SUPPORTED_EXTENSIONS:
                continue

            discovered_files.append(
                InputFile(
                    file_name=path.name,
                    stem=path.stem,
                    extension=path.suffix.lower(),
                    path=path,
                    size_bytes=path.stat().st_size,
                    created_at=datetime.fromtimestamp(
                        path.stat().st_ctime
                    ),
                    modified_at=datetime.fromtimestamp(
                        path.stat().st_mtime
                    ),
                    discovered_at=datetime.now()
                )
            )

        return discovered_files