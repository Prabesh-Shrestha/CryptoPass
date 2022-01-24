from cryptography.fernet import Fernet

def generate_key_en():
    
    file = open("haha.k", "wb")
    file.write(Fernet.generate_key())
    file.close()

if __name__ == "__main__":
    generate_key_en()