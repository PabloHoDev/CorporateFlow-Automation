from pathlib import Path
import os
import sys


def check_environment():
    required_vars = [
        "INPUT_PATH",
        "OUTPUT_PATH",
        "LOG_PATH",
        "BACKUP_PATH"
    ]

    missing = [
        var
        for var in required_vars
        if not os.getenv(var)
    ]

    if missing:
        raise RuntimeError(
            f"Variáveis ausentes: {missing}"
        )


def check_directories():

    directories = [
        os.getenv("INPUT_PATH"),
        os.getenv("OUTPUT_PATH"),
        os.getenv("LOG_PATH"),
        os.getenv("BACKUP_PATH")
    ]

    for directory in directories:

        path = Path(directory)

        if not path.exists():
            raise RuntimeError(
                f"Diretório inexistente: {path}"
            )


def main():

    try:

        check_environment()

        check_directories()

        print(
            "CorporateFlow container healthy"
        )

        sys.exit(0)

    except Exception as error:

        print(
            f"Health check failed: {error}"
        )

        sys.exit(1)


if __name__ == "__main__":
    main()