import sqlite3
from .crypto import dencrypt, encrypt
from .database import findByName, createTable, insertToTable
from tkinter import Tk, Label, Entry, Button
from PIL import ImageTk, Image
import clipboard
MainWindow = Tk()
MainWindow.title("CryptoPass")
logoimg = ImageTk.PhotoImage(Image.open("media/logo.png"))

try:
    dencrypt("password.db")
except:
    print("Couldnt Decrypt the Database")


connection = sqlite3.connect("password.db")
cursor = connection.cursor()


createTable(connection, cursor)
Label(MainWindow, image = logoimg).grid(row = 0, column =0, columnspan = 3)
Label(MainWindow, text = "Name of website:           Url of the website:         Password of Website:").grid(row = 1, column =0,columnspan = 3)
NewName = Entry(MainWindow)
NewUrl = Entry(MainWindow)
NewPassword = Entry(MainWindow)

NewName.grid(row = 2, column =0)
NewUrl.grid(row =2, column =1)
NewPassword.grid(row =2, column =2)
def Searchanddisplay(name):
    data =findByName(cursor, name)
    Nam,Url,Password = data
    Label(MainWindow, text = "Name of website:           Url of the website:         Password of Website:").grid(row = 5, column =0,columnspan = 3)
    data = Nam+"                            "+Url+"                                  "+Password
    Label(MainWindow,text =data).grid(row =6,column = 0,columnspan = 3)
    def copythat():
        clipboard.copy(Password)
    Button(MainWindow,text = "Copy", command = copythat).grid(row =6, column =3)

Button(MainWindow, text = "Add", command = lambda: insertToTable(connection, cursor, NewName.get(), NewUrl.get(), NewPassword.get() )).grid(row =2, column =3)
# searching data

Label(MainWindow, text = "Name of website:").grid(row = 3, column =0,columnspan = 3)
Name = Entry(MainWindow, width = 60, )
Name.grid(row = 4, column =0,columnspan = 3)



NewAddbutton = Button(MainWindow, text = "Search", command = lambda : Searchanddisplay(Name.get()))
NewAddbutton.grid(row =4, column =3)
conn.commit()


MainWindow.mainloop()
conn.close()

encrypt("password.db")
