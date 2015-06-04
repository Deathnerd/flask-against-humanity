# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, g, redirect, url_for, request, flash
from flask.ext.login import login_required

from .forms import AccountManagementForm
from ..models import User
from ..app import db
from ..utils import flash_errors


blueprint = Blueprint("humanity_user", __name__, url_prefix="/u", static_folder="../static")




@blueprint.route("/<string:user_name>/account", methods=['GET', 'POST'])
@login_required
def manage_user_account(user_name):
    if g.user.username != user_name:
        return redirect(url_for('public.index'))
    # Handle the changes to a user's account
    user = User.get_by_id(int(g.user.id))
    form = AccountManagementForm(request.form, gender=user.gender, active=user.active)
    if request.method == 'POST':
        if form.validate_on_submit():
            user.gender = form.gender.data
            user.active = form.active.data
            db.session.add(user)
            db.session.commit()
            flash("Account settings saved!", "success")
            return redirect(url_for('humanity_user.manage_user_account', user_name=g.user))
        else:
            flash_errors(form)
    return render_template("user/account.html", user=g.user, form=form)
