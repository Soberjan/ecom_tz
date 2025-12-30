from typing import List
from csv import DictReader

import psycopg2
from psycopg2 import sql
from fastapi import HTTPException
from pydantic import BaseModel, Field, ValidationError

from config import Config

class StudentRow(BaseModel):
    full_name: str
    subject: str
    grade: int = Field(ge=1, le=5)

class Database():
    """
    Класс для работы с базой данных
    """
    def connect(self, host: str = Config.db_host, db_name: str = Config.db_name, user: str = Config.db_user, password: str = Config.db_password):
        """
        Подключаемся к базе данных

        Args:
            host(str): Хост датабазы
            db_name(str): Имя датабазы
            user(str): Юзер датабазы
            password(str): Пароль датабазы
        """
        self.conn = psycopg2.connect(f"host={host} port=5432 dbname={db_name} user={user} password={password} ")
        self.cur = self.conn.cursor()
    
    def insert_entry(self, table: str, columns: List[str], values: List[str]):
        """
        Вставить запись в таблицу

        Args:
            table(str): таблица в которую вставляем запись
            columns(List[str]): какие колонки вставляем
            values(List[str]): какие значения вставляем
        """
        query = sql.SQL("""
            insert into {table} ({columns})
            values ({values})
            """
            ).format(
                    table=sql.Identifier(table),
                    columns=sql.SQL(', ').join(map(sql.Identifier, columns)),
                    values=sql.SQL(', ').join(sql.Placeholder() * len(columns)),
                    )
        self.cur.execute(query, values)
    
    def dump_to_db(self, reader: DictReader):
        """
        Скидываем инфу об учениках в базу данных

        Args:
            reader(DictReader): считанный csv файл
        """
        for row in reader:
            vals = list(row.values())
            try:
                _ = StudentRow(**row)
            except ValidationError as e:
                print(f"Ошибка в строке {row}: {e.errors()}")
                continue
            
            self.insert_entry('students', reader.fieldnames, vals)

        self.conn.commit()