import sys

from PySide6.QtWidgets import QApplication

from roll.core import init_database


def main() -> None:
    """Program entry point."""
    app = QApplication(sys.argv)
    app.setApplicationName("roll")
    app.setOrganizationName("roll")

    db = init_database()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
