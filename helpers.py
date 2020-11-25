from flask import *
from flask_sqlalchemy import *
from flask_mail import *

# Special chars for passwords
Specials = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-']

# Ensures a secure password
def check_password(Specials, password):
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password) or not any(char in Specials for char in password):
        return False
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return False
    else:
        return True
