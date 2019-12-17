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
        """
        method that confirms that the credentials account is a string and its available
        """
        for credentials in cls.User_list:
            if credentials.account == string:
                return credentials

    @classmethod
    def credentials_exists(cls, string):
        """
        method that helps to confirm the existence of the account and the returns boolean
        """
        for credentials in cls.User_list:
            if credentials.account == string:
                return True
        return False

    @classmethod
    def display_credentials(cls):
        """
        method that returns the User list
        """
        return cls.User_list

    @classmethod
    def copy_passwords(cls, string):
        password_found = User.find_by_account(string)
        pyperclip.copy(password_found.passwords)

    # @classmethod
    # def generate_password(cls):
    #     # length = int(plength)
    #      char = 'abcdefghijklmnopqrstuvwxyz1234567890'
    #      for p in range(4):
    #          passwordF = ''
    #         for c in range(length):
    #             passwordF += random.choice(char)
    #        print(passwordF)


class Account(object):
    pass
# password = input("into your password length required ")
# length = int(password)
# char = 'abcdefghijklmnopqrstuvwxyz1234567890'
# for p in range(4):
#     passwordF = ''
#     for c in range(length):
#         passwordF += random.choice(char)
#     print(passwordF)
