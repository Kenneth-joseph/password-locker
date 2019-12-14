import math
import random
import pyperclip


class Password(object):
    pass

    def __init__(self, first_name, phone, email):
        self.first_name = first_name
        self.phone = phone
        self.email = email


new_password = Password("KENT", "09", "kent@gmail")
print(new_password.email)

password = input("into your password length required ")
length = int(password)
char = 'abcdefghijklmnopqrstuvwxyz1234567890'
for p in range(4):
    passwordF=''
    for c in range(length):
     passwordF += random.choice(char)
    print(passwordF)