# -*- coding: utf-8 -*-

import os

REPO_NAME = "The-Ecosystem"  # Used for FREEZER_BASE_URL
DEBUG = True

SQLALCHEMY_DATABASE_URI = 'sqlite:///users.sqlite3'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Assumes the app is located in the same directory
# where this file resides
APP_DIR = os.path.dirname(os.path.abspath(__file__))

def parent_dir(path):
    '''Return the parent of a directory.'''
    return os.path.abspath(os.path.join(path, os.pardir))

PROJECT_ROOT = parent_dir(os.getcwd())
# In order to deploy to Github pages, you must build the static files to
# the project root
FREEZER_DESTINATION = os.getcwd()
# Since this is a repo page (not a Github user page),
# we need to set the BASE_URL to the correct url as per GH Pages' standards
FREEZER_BASE_URL = "http://gavinbm.github.com/The-Ecosystem"
FREEZER_REMOVE_EXTRA_FILES = False  # IMPORTANT: If this is True, all app files
                                    # will be deleted when you run the freezer
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite']
FLATPAGES_ROOT = os.path.join(os.getcwd(), 'pages')
FLATPAGES_EXTENSION = '.md'
