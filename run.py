#!/usr/bin/env python3.6
from password import User


def create_credentials(username, account, passwords):
    """
    this will help create new credentials
    """
    new_credentials = User(username, account, passwords)
    return new_credentials


def save_credentials(credentials):
    """
    function to save the credentials created
    """
    credentials.save_credrntials()
