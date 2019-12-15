import math
import random
import pyperclip


class User(object):
    User_list = []

    def __init__(self, username, account, passwords):
        self.username = username
        self.passwords = passwords
        self.account = account

    def save_details(self):
        User.User_list.append(self)


password = input("into your password length required ")
length = int(password)
char = 'abcdefghijklmnopqrstuvwxyz1234567890'
for p in range(4):
    passwordF = ''
    for c in range(length):
        passwordF += random.choice(char)
    print(passwordF)
