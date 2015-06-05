# -*- coding: utf-8 -*-
from .app import db
from flask.ext.login import UserMixin
from humanity.extensions import bcrypt
from .database import CRUDMixin, SurrogatePK


class User(db.Model, UserMixin, CRUDMixin, SurrogatePK):
    __tablename__ = "user"

    username = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=True)
    admin = db.Column(db.Boolean, default=False)
    active = db.Column(db.Boolean, default=True)

    def __init__(self, username, password=None, **kwargs):
        db.Model.__init__(self, username=username, **kwargs)
        if password:
            self.set_password(password)
        else:
            self.password = None

    def __repr__(self):
        return "{name}".format(name=self.username)

    def set_password(self, password):
        """Sets the password using bcrypt"""
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        """Checks the password"""
        return bcrypt.check_password_hash(self.password, value)

    def is_admin(self):
        """Is the user an administrator?"""
        return self.admin

    def is_active(self):
        """Is this user account active?"""
        return self.active

    def get_id(self):
        """Convenience Method to get the current user's id"""
        return self.id