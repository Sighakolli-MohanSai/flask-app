import os
import mysql.connector

def get_connection():

    connection = mysql.connector.connect(

        host=os.getenv("DB_HOST", "db"),

        user=os.getenv("DB_USER", "root"),

        password=os.getenv("DB_PASSWORD", "root123"),

        database=os.getenv("DB_NAME", "movie_db")

    )

    return connection