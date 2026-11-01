from generator import generate_password
from strength_checker import check_strength
from entropy import calculate_entropy
from crypto_utils import sha256_hash
from storage import save_password, read_passwords
from generator import generate_password, generate_pattern_password, generate_smart_password


def menu():
    print("\n🔐 Secure Password Manager")
    print("1. Generate Password")
    print("2. Save Password")
    print("3. Smart Readable Password")
    print("4. View Saved Passwords")
    print("5. Exit")

while True:
    menu()
    choice = input("Choose option: ")

    if choice == "1":
        length = int(input("Length: "))
        pwd = generate_password(length, True, True, True, True)
        print("Generated:", pwd)
        print("Strength:", check_strength(pwd))
        print("Entropy:", calculate_entropy(pwd), "bits")
        print("SHA-256:", sha256_hash(pwd))

    elif choice == "2":
        master = input("Master Password: ")
        site = input("Site: ")
        user = input("Username: ")
        pwd = input("Password: ")
        save_password(master, site, user, pwd)
        print("Saved securely!")

    elif choice == "3":
        pwd = generate_smart_password()
        print("Generated:", pwd)
        print("Strength:", check_strength(pwd))
        print("Entropy:", calculate_entropy(pwd), "bits")
        print("SHA-256:", sha256_hash(pwd))


    elif choice == "4":
        break
