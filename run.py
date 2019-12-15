#!/usr/bin/env python3.6
from password import User


def create_credentials(username, account, passwords):
    """
    this will help create new credentials
    """
    new_credentials = User(username, account, passwords)
    return new_credentials


def save_details(credentials):
    """
    function to save the credentials created
    """
    credentials.save_details()


def delete_credentials(credentials):
    credentials.delete_credentials()


def find_credentials(string):
    return User.find_by_account(string)


def check_availability(string):
    return User.credentials_exists(string)


def display_credential():
    return User.display_credentials()


def main():
    print("hello welcome to your password locker account, what is your name?")
    user_name = input()
    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : cc - create a new credentials, dc - display credentials, fc -find a contact, "
              "ex -exit the contact list ")

