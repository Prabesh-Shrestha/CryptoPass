
import sqlite3

import crypto
from tkinter import *
from PIL import ImageTk, Image
import clipboard
MainWindow = Tk()
MainWindow.title("CryptoPass")
logoimg = ImageTk.PhotoImage(Image.open("media/logo.png"))


try:
    crypto.dencrypt("password.db")
except:
    pass


conn = sqlite3.connect("password.db")
c = conn.cursor()

def createTable():
    c.execute("""CREATE TABLE passwords (
                Name text,
                url text,
                pass text
    )""")
    conn.commit()


try:    
    createTable()
except:
    pass

def insertToTable(name, url, password):
    c.execute("INSERT INTO passwords VALUES ('"+name+"', '"+url+"', '"+password+"')")
    conn.commit()
def findByName(name):
    try:
        c.execute("SELECT * FROM passwords WHERE name = '"+name+"'")
    except:
        pass
    return c.fetchone()
insertToTable("Facebook", "haha yas", "haah ")
# print(findByName("Facebook"))
logolabel = Label(MainWindow, image = logoimg).grid(row = 0, column =0, columnspan = 3)
# adding data
Label(MainWindow, text = "Name of website:           Url of the website:         Password of Website:").grid(row = 1, column =0,columnspan = 3)
NewName = Entry(MainWindow)
NewName.grid(row = 2, column =0)
NewUrl = Entry(MainWindow)
NewUrl.grid(row =2, column =1)
NewPassword = Entry(MainWindow)
NewPassword.grid(row =2, column =2)
def addData():
    name = NewName.get()
    url = NewUrl.get()
    password = NewPassword.get()
    print(name, url, password)
    insertToTable(name, url, password)


Addbutton = Button(MainWindow, text = "Add", command = addData).grid(row =2, column =3)
# searching data
Label(MainWindow, text = "Name of website:").grid(row = 3, column =0,columnspan = 3)
Name = Entry(MainWindow, width = 60)
Name.grid(row = 4, column =0,columnspan = 3)


def Searchanddisplay():
    name = Name.get()
    data =findByName(name)
    Nam,Url,Password = data
    Label(MainWindow, text = "Name of website:           Url of the website:         Password of Website:").grid(row = 5, column =0,columnspan = 3)

    data = Nam+"                            "+Url+"                                  "+Password
    Label(MainWindow,text =data).grid(row =6,column = 0,columnspan = 3)
    def copythat():
        clipboard.copy(Password)
    button = Button(MainWindow,text = "Copy", command = copythat)
    button.grid(row =6, column =3)

NewAddbutton = Button(MainWindow, text = "Search", command = Searchanddisplay).grid(row =4, column =3)
conn.commit()


MainWindow.mainloop()
crypto.encrypt("password.db")
conn.close()
