import math
import random
import pyperclip


class User(object):
    User_list = []

    def __init__(self, username, password):
        self.username = username
        self.password = password


password = input("into your password length required ")
length = int(password)
char = 'abcdefghijklmnopqrstuvwxyz1234567890'
for p in range(4):
    passwordF = ''
    for c in range(length):
        passwordF += random.choice(char)
    print(passwordF)
