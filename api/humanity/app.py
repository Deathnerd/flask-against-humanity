# -*- coding: utf-8 -*-
from flask import Flask
from .settings import Production
from .extensions import bcrypt, db, migrate, debug_toolbar, admin, login_manager, assets
from .models import User
from .errors import RequestErrors
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.assets import Bundle
import user
import public


def register_assets():
    """
    Register the static assets to be minimized with Flask-Assets
    TODO: Get it working right :/
    :return None:
    """
    js = Bundle('assets/plugins/jquery-1.11.1.min.js',
                'assets/plugins/jquery-migrate-1.2.1.min.js',
                'assets/plugins/jquery.easing.1.3.js',
                'assets/plugins/jquery-scrollTo/jquery.scrollTo.min.js',
                'assets/plugins/prism/min/prism-min.js',
                'assets/js/min/main-min.js',
                filters='jsmin', output='assets/packed/site.js')
    css = Bundle('assets/plugins/bootstrap/css/bootstrap.min.css',
                 'assets/plugins/font-awesome/css/font-awesome.css',
                 'assets/plugins/prism/min/prism.css',
                 'assets/css/styles-4.css',
                 filters='cssmin', output='assets/packed/site.css')

    assets.register('js_all', js)
    assets.register('css_all', css)
    return None


def create_app(config_object=Production):
    """
    Application factory following the pattern at:
    http://flask.pocoo.org/docs/patterns/appfactories/

    :param config_object: The configuration object that we'll be using
    :returns app:
    """
    app = Flask(__name__)
    app.config.from_object(config_object)

    # Register stuff to the app
    register_extensions(app)
    register_admin(User,
                   session=db.session)
    register_blueprints(app)
    # register_assets()

    # Configuration
    configure_login()

    errors = RequestErrors()
    errors.init_app(app)

    # admin requires a custom setup
    # admin_views()
    return app


def register_extensions(app):
    """
    Given an app object, initialize the application extensions
    :param app: The current application
    :returns None:
    """
    bcrypt.init_app(app)
    db.init_app(app)
    migrate.init_app(app, db)
    debug_toolbar.init_app(app)
    admin.init_app(app)
    login_manager.init_app(app)
    # assets.init_app(app)
    return None


def register_blueprints(app):
    """
    Given an app object, initialize the blueprints
    :param app: The current application
    :return None:
    """
    app.register_blueprint(user.blueprint)
    app.register_blueprint(public.blueprint)
    return None


def register_admin(*args, **kwargs):
    """
    Takes in any number of unnamed args assuming they're database model classes
    and registers them with the SuperAdmin
    :returns None:
    """
    for model in args:
        admin.add_view(ModelView(model, kwargs['session']))
    return None


def admin_views():
    return None


def configure_login():
    login_manager.login_view = "public.login"