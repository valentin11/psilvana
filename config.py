import os

DEBUG = False
CSRF_ENABLED = True
SECRET_KEY = '#2#e1r%$e#7#!5@g#&.I^1D@S-$x1Z2c_5.'
SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
SQLALCHEMY_TRACK_MODIFICATIONS = False

