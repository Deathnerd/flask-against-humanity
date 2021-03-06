# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, PasswordField, SelectField, BooleanField
from wtforms.validators import DataRequired, Email, Length
from ..models import User

class RegisterForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=40)])
    confirm = PasswordField('Verify password', validators=[DataRequired(), Length(min=6, max=40)])
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')])

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        """
        Performs registration validation. Checks for duplicate user and email as well as required fields
        :return:
        """
        initial_validation = super(RegisterForm, self).validate() and self.password != self.confirm
        if not initial_validation:
            return False
        user = User.query.filter_by(username=self.username.data).first()
        if user:
            self.username.errors.append("Username already registered")
            return False
        return True


class LoginForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me', default=False)

    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        """
        Performs login validation. Checks the user password, that the username exists, and that the user is active.
        Also checks the login fields match what's required
        :return:
        """
        initial_validation = super(LoginForm, self).validate()
        if not initial_validation:
            return False

        self.user = User.query.filter_by(username=self.username.data).first()
        if not self.user:
            self.username.errors.append('Unknown username')
            return False

        if not self.user.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False

        if not self.user.active:
            self.username.errors.append('User not activated')
            return False

        return True
