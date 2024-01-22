
def createTable(connection, cursor):
    cursor.execute("""CREATE TABLE passwords (
                Name text,
                url text,
                pass text
    )""")
    connection.commit()

def insertToTable(connection, cursor, name, url, password):
    cursor.execute("INSERT INTO passwords VALUES ('"+name+"', '"+url+"', '"+password+"')")
    connection.commit()

def findByName(cursor, name):
    try:
        cursor.execute("SELECT * FROM passwords WHERE name = '"+name+"'")
    except:
        pass
    return cursor.fetchone()
