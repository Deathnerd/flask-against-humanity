# -*- coding: utf-8 -*-
import os


class Base():
    """Base Config"""
    # General App
    ENV = os.environ.get('HUMANITY_SERVER_ENV', 'development')
    SECRET_KEY = os.environ.get('HUMANITY_SECRET_KEY', 'S00p3rS3cr3t')
    APP_DIR = os.path.abspath(os.path.dirname(__file__))
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))

    # SQLAlchemy
    SQLALCHEMY_DATABASE_URI = "mysql://{}:{}@{}/{}?charset=utf8".format(os.environ.get('HUMANITY_DATABASE_USER', 'humanity'),
                                                                        os.environ.get('HUMANITY_DATABASE_PASS', 'humanity'),
                                                                        os.environ.get('HUMANITY_DATABASE_HOST', 'localhost'),
                                                                        os.environ.get('HUMANITY_DATABASE_NAME', 'humanity-dev'))

    # Bcrypt
    BCRYPT_LOG_ROUNDS = 13

    # Debug Toolbar
    DEBUG_TB_ENABLED = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # Flask-Assets
    ASSETS_DEBUG = False

    # WTForms
    WTF_CSRF_ENABLED = True
    WTF_CSRF_SECRET_KEY = os.environ.get('HUMANITY_WTF_CSRF_SECRET_KEY', 'wtfthisissecret')
    RECAPTCHA_PUBLIC_KEY = os.environ.get('HUMANITY_RECAPTCHA_PUBLIC_KEY', 'thisispublic')
    RECAPTCHA_PRIVATE_KEY = os.environ.get('HUMANITY_RECAPTCHA_PRIVATE_KEY', 'thisisprivate')


class Production(Base):
    """Production Config"""
    DEBUG = False
    DEBUG_TB_ENABLED = False


class Development(Base):
    """Development Config"""
    # General App
    DEBUG = True

    # SQLAlchemy

    # Debug Toolbar
    DEBUG_TB_ENABLED = True
    DEBUG_TB_PROFILER_ENABLED = True
    # DEBUG_TB_INTERCEPT_REDIRECTS = True
    DEBUG_TB_TEMPLATE_EDITOR_ENABLED = True

    # Flask-Assets
    # ASSETS_DEBUG = True

    # WTF-Forms


class Staging(Base):
    """Staging Config"""
    # General App
    TESTING = True
    DEBUG = True

    # Bcrypt
    BCRYPT_LOG_ROUNDS = 1

    # WTForms