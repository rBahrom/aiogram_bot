# db.py module
import os

import psycopg2 as psql

class Database:
    @staticmethod
    async def connect(query, query_type):
        db = psql.connect(
            database=os.getenv("db_data"),
            user=os.getenv("db_user"),
            password=os.getenv("password"),
            host=os.getenv("db_host"),
            port=os.getenv("db_port")
        )
        cursor = db.cursor()
        data = ["insert", "delete"]
        cursor.execute(query)
        if query_type in data:
            db.commit()
            if query_type == "insert":
                return "inserted successfully"
        else:
            return cursor.fetchall()

    @staticmethod
    async def check_user_id(user_id: int):
        query = f"SELECT * FROM bot WHERE user_id = {user_id}"
        check_user = await Database.connect(query, query_type="select")
        if len(check_user) == 1:
            print("> > > > > > ", check_user)
            return True
        return False

