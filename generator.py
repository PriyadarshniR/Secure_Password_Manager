import random
import string

# 🔹 1. Fully random password
def generate_password(length, upper, lower, digits, symbols):
    chars = ""
    if upper:
        chars += string.ascii_uppercase
    if lower:
        chars += string.ascii_lowercase
    if digits:
        chars += string.digits
    if symbols:
        chars += string.punctuation

    if not chars:
        return "Select at least one option!"

    return ''.join(random.choice(chars) for _ in range(length))


# 🔹 2. Pattern-style password (word + numbers + symbols)
def generate_pattern_password(word, num_digits=3, num_symbols=2):
    numbers = ''.join(random.choice(string.digits) for _ in range(num_digits))
    symbols = ''.join(random.choice(string.punctuation) for _ in range(num_symbols))
    return word + numbers + symbols


# 🔹 3. Smart readable random password
def generate_smart_password():
    letters = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3,6)))
    numbers = ''.join(random.choice(string.digits) for _ in range(random.randint(1,4)))
    symbols = ''.join(random.choice(string.punctuation) for _ in range(random.randint(1,2)))

    parts = [letters, numbers, symbols]
    random.shuffle(parts)

    return ''.join(parts)
