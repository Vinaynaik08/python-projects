import random
import string

print("Password Generator")

length = int(input("Length Of the Password: "))

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

all_chars = letters + digits + symbols

password_list = []

for i in range(length):
    random_char = random.choice(all_chars)
    password_list.append(random_char)

password = "".join(password_list)

print(password)