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
        print("Use these short codes : cc - create a new credentials, dc - display credentials, fc -find a "
              "credentials, "
              "ex -exit the credentials list ")
        short_code = input().lower()
        if short_code == 'cc':
            print("new credentials")
            print("-" * 10)
            print("username")
            username = input()
            print("enter the account")
            account = input()
            print("enter password")
            password = input()
            save_details(create_credentials(username, account, password))  # creating new credentials
            print('\n')
            print(f"new credentials for {account} is created")
            print('\n')
        elif short_code == 'dc':
            if display_credential():
                print("here is a list of all your credentials")
