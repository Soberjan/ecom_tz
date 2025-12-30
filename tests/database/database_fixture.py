import pytest
import os

from src.database.database import Database

@pytest.fixture
def database(config):
    db = Database()
    db.connect(db_name=config.db_name, host=config.db_host, user=config.db_user, password=config.db_password)

    db.cur.execute("""
                DROP SCHEMA IF EXISTS testing CASCADE;
                CREATE SCHEMA testing;
                """)

    db.cur.execute('SET search_path TO testing;')
    for file in sorted(os.listdir("migrations")):
        with open(os.path.join('migrations/', file), 'r') as query:
            db.cur.execute(query.read())
    db.conn.commit()
    
    yield db
    
    db.conn.commit()
    db.conn.close()

@pytest.fixture
def filled_db(database):
    for i in range(4):
        database.insert_entry('students', ['full_name', 'subject', 'grade'], ['Вася', 'русский', 2])
    database.conn.commit()
    yield database