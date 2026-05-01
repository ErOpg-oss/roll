import logging
from pathlib import Path

from PySide6.QtCore import QDir, QStandardPaths
from PySide6.QtSql import QSqlDatabase, QSqlQuery

logger = logging.getLogger(__name__)


def init_database() -> QSqlDatabase:
    db_name = "attendance.db"
    path = QStandardPaths.writableLocation(
        QStandardPaths.StandardLocation.AppDataLocation
    )
    _ = QDir().mkpath(path)
    db_file = path / Path(db_name)

    logger.info("Opening database")

    db = QSqlDatabase.addDatabase("QSQLITE")
    db.setDatabaseName(str(db_file))

    if not db.open():
        logger.error("SQL Error: %s", db.lastError().text())

    logger.info("Opened database")

    logger.info("Setupping foreign keys")

    query = QSqlQuery()
    if not query.exec("PRAGMA foreign_keys = ON;"):
        logger.error("SQL Error: %s", query.lastError().text())

    logger.info("Setupped foreign keys")

    _create_schema_if_needed()

    return db


def _create_schema_if_needed() -> None:
    root_dir = Path(__file__).parent.parent
    sql_path = root_dir / "queries" / "on_init.sql"

    query = QSqlQuery()
    with Path(sql_path).open() as file:
        sql_text = "".join(file.readlines())
    queries = [q.strip() + ";" for q in sql_text.split(";") if q.strip()]
    logger.info("Creating tables...")
    for sql in queries:
        if not query.exec(sql):
            logger.error("SQL Error: %s", query.lastError().text())
    logger.info("Created tables")
