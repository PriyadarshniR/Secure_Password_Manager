from crypto_utils import get_fernet

FILE = "passwords.db"

def save_password(master_password, site, username, password):
    f = get_fernet(master_password)
    data = f"{site}|{username}|{password}\n"
    encrypted = f.encrypt(data.encode())

    with open(FILE, "ab") as file:
        file.write(encrypted + b"\n")

def read_passwords(master_password):
    f = get_fernet(master_password)
    entries = []

    try:
        with open(FILE, "rb") as file:
            for line in file:
                decrypted = f.decrypt(line.strip()).decode()
                entries.append(decrypted)
    except:
        return ["Wrong master password or no data"]

    return entries
