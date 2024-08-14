import sqlite3
from database.queries import Queries


class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute(Queries.CREATE_SURVEY_RESULTS_TABLE)

            conn.commit()

    def execute(self, query: str, params: tuple):
        with sqlite3.connect(self.path) as conn:
            conn.execute(query, params)

            conn.commit()

# conn.execute(
#     query='''INSERT INTO book_survey (name, age, gender, genre) VALUES
#     (?, ?, ?, ?)''', params=('fatima', 16, 'female', 'romance')
# )
