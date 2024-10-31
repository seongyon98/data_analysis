import mysql.connector
import db.query as mysql_query
from sqlalchemy import create_engine


class DBconnector:
    def __init__(
        self, engine, orm_engine, host, database, user, password, port, **options
    ):
        self.engine = engine
        self.orm_engine = orm_engine
        self.conn_params = {
            "host": host,
            "database": database,
            "user": user,
            "password": password,
            "port": port,
        }

        if "OPTIONS" in options:
            if "charset" in options["OPTIONS"]:
                self.conn_params["charset"] = options["OPTIONS"]["charset"]
            if "collation" in options["OPTIONS"]:
                self.conn_params["collation"] = options["OPTIONS"]["collation"]

        self.orm_conn_params = (
            f"{orm_engine}://{user}:{password}@{host}:{port}/{database}"
        )
        self.orm_connect()

        if self.engine == "mysql":
            self.connect = self.mysql_connect()
            self.queries = mysql_query.queries

    def __enter__(self):
        print("접속")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("종료")

    def mysql_connect(self):
        self.conn = mysql.connector.connect(**self.conn_params)
        return self.conn

    def orm_connect(self):
        self.orm_conn = create_engine(self.orm_conn_params)
        return self.orm_conn

    def get_query(self, table_name):
        _query = self.queries[table_name]
        return _query
