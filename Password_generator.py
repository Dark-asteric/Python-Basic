import random
import string
import secrets

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

n = int(input())
password = ""
for i in range(n):
	password += ''.join(secrets.choice(alphabet))
print(f"Your password is here : {password}")