#!/usr/bin/env python3.6
import string

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


def find_by_account(string):
    return User.find_by_account(string)


def credential_exists(string):
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
                print('\n')

                for credentials in display_credential():
                    print(f"{credentials.username} {credentials.account} {credentials.passwords}")
                    print('\n')
                else:
                    print('\n')
                    print("you don't seem to have any account saved yet")
                    print('\n')

        elif short_code == 'fc':
            print("enter the account you want to search for")
            account = input()
            if find_by_account(string):
                search_credentials = find_by_account(account)
                print(f"{search_credentials.username} {search_credentials.account} {search_credentials.passwords}")
                print('_' * 20)

            else:
                print("credentials doesnt exist")
        elif short_code == 'ex':
            print("bye....")

            break
        else:
            print("I didn't quite catch that please use the short codes provided")


if __name__ == '__main__':
    main()
