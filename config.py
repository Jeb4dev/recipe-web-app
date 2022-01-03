"""Flask app configuration."""
from os import environ, path

basedir = path.abspath(path.dirname(__file__))


class Config:
    """Set Flask configuration from environment variables."""

    FLASK_APP = 'wsgi.py'
    FLASK_ENV = environ.get('FLASK_ENV')
    SECRET_KEY = environ.get('SECRET_KEY') or '%#MPWNINVPAIBI08h029h7fpq4npf3p2+9hnpNO&F&VO'

    # Static Assets
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    COMPRESSOR_DEBUG = environ.get('COMPRESSOR_DEBUG')

    # Flask-SQLAlchemy
    DB_NAME = "database.db"
    db_url = environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI: str = environ.get('DATABASE_URL', 'sqlite:///app.db').replace('postgres', 'postgresql')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
