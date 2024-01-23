from cryptography.fernet import Fernet


def generate_key():
    file = open("key", "wb")
    file.write(Fernet.generate_key())
    file.close()


if __name__ == "__main__":
    generate_key()
