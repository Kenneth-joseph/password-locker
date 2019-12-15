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

    def delete_credential(self):
        User.User_list.remove(self)

    @classmethod
    def find_by_account(cls, string):
        for credentials in cls.User_list:
            if credentials.account == string:
                return credentials

    @classmethod
    def credentials_exists(cls,string):
        for credentials in cls.User_list:
            if credentials.account == string:
                return True
        return False
# password = input("into your password length required ")
# length = int(password)
# char = 'abcdefghijklmnopqrstuvwxyz1234567890'
# for p in range(4):
#     passwordF = ''
#     for c in range(length):
#         passwordF += random.choice(char)
#     print(passwordF)
