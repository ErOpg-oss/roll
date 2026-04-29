import logging
from pathlib import Path

from PySide6.QtCore import QDir, QStandardPaths
from PySide6.QtSql import QSqlDatabase, QSqlQuery

logging.basicConfig(level=logging.ERROR, filename="app.log")


def init_database() -> QSqlDatabase:
    db_name = "attendance.db"
    path = QStandardPaths.writableLocation(
        QStandardPaths.StandardLocation.AppDataLocation
    )
    _ = QDir().mkpath(path)
    db_file = path / Path(db_name)

    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(str(db_file))

    if not db.open():
        logging.error(f"SQL Error: {db.lastError().text()}")

    _create_schema_if_needed(db)

    return db


def _create_schema_if_needed(db: QSqlDatabase) -> None:
    query = QSqlQuery(db)
    sql = """
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER,
        isbn TEXT,
        genre TEXT,
        status TEXT NOT NULL DEFAULT 'to_read',
        rating INTEGER DEFAULT 0,
        pages INTEGER,
        notes TEXT,
        added_at TEXT NOT NULL DEFAULT (datetime('now'))
    )
    """
    if not query.exec(sql):
        logging.error(f"SQL Error: {query.lastError().text()}")
