import psycopg2
import db.pgsql_query as postgresql_query
from sqlalchemy import create_engine


class DBconnector:
    def __init__(self, engine, orm_engine, host, database, user, password, port):
        self.engine = engine
        self.orm_engine = orm_engine
        self.conn_params = dict(
            host=host, dbname=database, user=user, password=password, port=port
        )
        self.orm_conn_params = (
            f"{orm_engine}://{user}:{password}@{host}:{port}/{database}"
        )
        self.orm_connect()

        if self.engine == "postgresql":
            self.connect = self.postgres_connect()
            self.queries = postgresql_query.queries

    def __enter__(self):
        print("접속")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("종료")

    def postgres_connect(self):
        self.conn = psycopg2.connect(**self.conn_params)
        return self

    def orm_connect(self):
        self.orm_conn = create_engine(self.orm_conn_params)
        return self.orm_conn

    def get_query(self, table_name):
        _query = self.queries[table_name]
        return _query
