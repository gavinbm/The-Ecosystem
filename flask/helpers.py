from flask import Flask, redirect, url_for, render_template, request, session, flash
import sqlalchemy

app = Flask(__name__)
app.secret_key = "howdy"

with open("accounts.json") as f:
    Users = json.load(f)

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

# Checks if a username already exists
def check_username(Users, name):
    check = True
    for user in Users:
        if user["name"] == name:
            check = False
    return check

# Finds a user
def find_user(Users, name, password):
    check = False
    for user in Users:
        if user["name"] == name and user["password"] == password:
            check = True
    return check

# Creates a user
def create_user(name, password):
    user = {'name':name, 'password':password, 'games':[]}
    Users.append(user)
    with open("accounts.txt", "w") as fout:
            json.dump(Users, fout)
