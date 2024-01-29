from .database import findByName, insertToTable
from tkinter import Tk, Label, Entry, Button
from PIL import ImageTk, Image


def load_ui(connection, cursor):
    def Searchanddisplay(name):
        name, url, password = findByName(cursor, name)
        Label(
            Window,
            text="Name of website:           Url of the website:         Password of Website:",
        ).grid(row=5, column=0, columnspan=3)
        data = (
            name
            + "                            "
            + url
            + "                                  "
            + password
        )
        Label(Window, text=data).grid(row=6, column=0, columnspan=3)
        Button(
            Window, text="Copy", command=lambda: Window.clipboard_get()
        ).grid(row=6, column=3)

    Window = Tk()
    Window.title("CryptoPass")

    Logo = ImageTk.PhotoImage(Image.open("media/logo.png"))
    Label(Window, image=Logo).grid(row=0, column=0, columnspan=3)

    Label(
        Window,
        text="Name of website:           Url of the website:         Password of Website:",
    ).grid(row=1, column=0, columnspan=3)

    NewName = Entry(Window)
    NewUrl = Entry(Window)
    NewPassword = Entry(Window)

    NewName.grid(row=2, column=0)
    NewUrl.grid(row=2, column=1)
    NewPassword.grid(row=2, column=2)

    AddButton = Button(
        Window,
        text="Add",
        command=lambda: insertToTable(
            connection, cursor, NewName.get(), NewUrl.get(), NewPassword.get()
        ),
    )
    AddButton.grid(row=2, column=3)

    Label(Window, text="Name of website:").grid(row=3, column=0, columnspan=3)

    Name = Entry(
        Window,
        width=60,
    )
    Name.grid(row=4, column=0, columnspan=3)

    Button(
        Window, text="Search", command=lambda: Searchanddisplay(Name.get())
    ).grid(row=4, column=3)

    return Window
