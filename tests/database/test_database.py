from tests.database.database_fixture import database

def test_insert_entry(database):
    database.insert_entry('students', ['full_name', 'subject', 'grade'], ['Вася', 'русский', 2])
    
    database.cur.execute("""
                SELECT *
                FROM students
                """)

    s = database.cur.fetchone()
    assert s[1] == 'Вася'
    assert s[2] == 'русский'
    assert s[3] == 2
    