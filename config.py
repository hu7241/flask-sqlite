"""
This script contains flask app settings
"""
import os
BASEDIR = os.path.abspath(os.path.dirname(__file__))
DBNAME = "app.db"


class Config(object):
    DATABASE_NAME = DBNAME
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASEDIR, DBNAME)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = True
    DATA_URL = 'https://gist.githubusercontent.com/curran/a08a1080b88344b0' \
               'c8a7/raw/d546eaee765268bf2f487608c537c05e22e4b221/iris.csv'
