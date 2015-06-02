# -*- coding: utf-8 -*-
from flask_wtf import Form
from wtforms import StringField, SelectField, BooleanField
from wtforms.validators import DataRequired, Email, Length


class AccountManagementForm(Form):
    username = StringField('Username', validators=[DataRequired(), Length(min=6, max=50)])
    active = BooleanField('Account Active')
    gender = SelectField('Gender', choices=[('male', 'Male'), ('female', 'Female')])

    def __init__(self, *args, **kwargs):
        super(AccountManagementForm, self).__init__(*args, **kwargs)
        self.user = None

    def validate(self):
        """
        Validates that the user has all the information needed in their account page
        :return:
        """
        return super(AccountManagementForm, self).validate()