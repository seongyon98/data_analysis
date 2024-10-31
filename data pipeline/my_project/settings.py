import os
import dotenv

env_path = dotenv.find_dotenv()
dotenv.load_dotenv(env_path)

TEMP_PATH = "d:\\bigdata9_seungyeon\\hadoop_p\\my_project\\temp_storage"

DB_SETTINGS = {
    "POSTGRES": {
        "engine": os.getenv("POSTGRES_ENGINE"),
        "orm_engine": "postgresql+psycopg2",
        "host": os.getenv("POSTGRES_HOST"),
        "database": os.getenv("POSTGRES_DB"),
        "user": os.getenv("POSTGRES_USER"),
        "password": os.getenv("POSTGRES_PASSWORD"),
        "port": os.getenv("POSTGRES_PORT"),
    },
}
