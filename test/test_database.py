import database
from database import get_connection


def test_get_connection(tmp_path, monkeypatch):
    database_dir = tmp_path / "database"
    database_path = database_dir / "test.db"

    monkeypatch.setattr(database, "DATABASE_DIR", database_dir)
    monkeypatch.setattr(database, "DATABASE_PATH", database_path)

    connection = get_connection()

    assert connection is not None
    assert database_dir.exists()

    connection.close()