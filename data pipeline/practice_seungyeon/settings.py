import os
import dotenv

env_path = dotenv.find_dotenv()
dotenv.load_dotenv(env_path)

TEMP_PATH = "d:\\bigdata9_seungyeon\\hadoop_p\\practice_seungyeon\\temp_storage"

DB_SETTINGS = {
    "MYSQL": {
        "engine": os.getenv("MYSQL_ENGINE"),
        "orm_engine": "mysql+mysqlconnector",
        "host": os.getenv("MYSQL_HOST"),
        "database": os.getenv("MYSQL_DB"),
        "user": os.getenv("MYSQL_USER"),
        "password": os.getenv("MYSQL_PASSWORD"),
        "port": os.getenv("MYSQL_PORT"),
        "OPTIONS": {
            "charset": "utf8mb4",
            "collation": "utf8mb4_unicode_ci",  # 여기에서 collation 설정
        },
    },
}
