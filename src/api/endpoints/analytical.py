from fastapi import APIRouter, Request, Query
from typing import Dict, List, Tuple, Union
from pydantic import BaseModel

from database.queries import analytics
from database.database import Database

analytical_router = APIRouter(tags=["Analytics"])

def execute_query(db: Database, query: str, params: Tuple[str] = ()):
    db.cur.execute(query, params)
    return db.cur.fetchall()

class OutputModel(BaseModel):
    result: List[Dict[str, Union[str, int]]]

@analytical_router.get(
    "/students/more-than-3-twos",
    summary="Количество новых резюме",
    description="Возвращает общее количество новых резюме, добавленных в систему.",
    response_model=OutputModel
)
def more_than_3_twos(request: Request):
    rows = execute_query(request.app.state.db, analytics.more_than_3_twos_query)
    columns = ['full_name', 'count_twos']
    res = [dict(zip(columns, row)) for row in rows]
    return {'result': res}

@analytical_router.get(
    "/students/less-than-5-twos",
    summary="Количество новых резюме",
    description="Возвращает общее количество новых резюме, добавленных в систему.",
    response_model=OutputModel
)
def less_than_5_twos(request: Request):
    rows = execute_query(request.app.state.db, analytics.less_than_5_twos_query)
    columns = ['full_name', 'count_twos']
    res = [dict(zip(columns, row)) for row in rows]
    return {'result': res}
