from tests.database.database_fixture import database, filled_db
import src.database.queries.analytics as queries

def test_analytics_queries(filled_db):
    filled_db.cur.execute(queries.less_than_5_twos_query)
    
    s = filled_db.cur.fetchone()
    assert s[0] == 'Вася'
    assert s[1] == 4
    
    filled_db.cur.execute(queries.more_than_3_twos_query)
    
    s = filled_db.cur.fetchone()
    assert s[0] == 'Вася'
    assert s[1] == 4