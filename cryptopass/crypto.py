from cryptography.fernet import Fernet
import random
import string


def read_key():
    file = open("haha.k", "rb")
    key = file.read()
    file.close()
    return key


def encrypt(filename):
    with open(filename, "rb") as f:
        data = f.read()
    fernet = Fernet(read_key())
    with open(filename, "wb") as f:
        f.write(fernet.encrypt(data))
    f.close()


def dencrypt(filename):
    with open(filename, "rb") as f:
        data = f.read()
    fernet = Fernet(read_key())
    dencrypts = fernet.decrypt(data)
    with open(filename, "wb") as f:
        f.write(dencrypts)


def generate_password():
    letters = "".join((random.choice(string.ascii_letters) for i in range(10)))
    digits = "".join((random.choice(string.digits) for i in range(5)))

    sample_list = list(letters + digits)
    random.shuffle(sample_list)
    return "".join(sample_list)
