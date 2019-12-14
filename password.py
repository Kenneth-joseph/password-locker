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

password=input("into your password length required ")
length=int(password)
print(length*2)

