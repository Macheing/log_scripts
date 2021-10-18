#!/usr/bin/ python3

def validate_user(username):
    minlength = 3 # user name should at least be 3 characters long.
    assert type(username) == str, 'User name must be of type string not a integer or a list!'
    if len(username) < minlength:
        return False # minimum length must be at least 3 characters long.
    elif not username.isalnum():
        return False

    return True