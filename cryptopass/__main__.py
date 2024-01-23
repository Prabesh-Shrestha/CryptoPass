from .database import startConnection, endConnection
from .ui import load_ui

def main():
    connection, cursor = startConnection()
    load_ui(connection, cursor).mainloop()
    endConnection(connection)

main()
