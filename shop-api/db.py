import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="shop-db.c7c22480exdf.eu-west-1.rds.amazonaws.com",
        user="admin",
        password="Muhirwajd1!",
        database="shop"
    )

