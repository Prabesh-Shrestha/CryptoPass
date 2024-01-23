from .crypto import dencrypt, encrypt
from .key import generate_key

import sqlite3
def createTable(connection, cursor):
    cursor.execute(
        """CREATE TABLE passwords (
                Name text,
                url text,
                pass text
    )"""
    )
    connection.commit()


def insertToTable(connection, cursor, name, url, password):
    cursor.execute(
        "INSERT INTO passwords VALUES ('"
        + name
        + "', '"
        + url
        + "', '"
        + password
        + "')"
    )
    connection.commit()


def findByName(cursor, name):
    try:
        cursor.execute("SELECT * FROM passwords WHERE name = '" + name + "'")
    except:
        pass
    return cursor.fetchone()

def startConnection():
    file = True
    try:
        dencrypt("password.db")
    except:
        file = False
        print("Couldnt Decrypt the Database")
    connection = sqlite3.connect("password.db")
    cursor = connection.cursor()
    if not file:
        createTable(connection, cursor)
        generate_key()
    return (connection, cursor)

def endConnection(connection): 
    connection.close()
    encrypt("password.db")

