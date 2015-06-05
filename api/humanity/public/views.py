# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, g, redirect, url_for, request, flash, jsonify
from flask.ext.login import login_user, logout_user, login_required
from .forms import RegisterForm, LoginForm
from ..models import User
from ..utils import flash_errors
from ..extensions import login_manager

blueprint = Blueprint("public", __name__, static_folder="../static")


@login_manager.user_loader
def load_user(id):
    """
    Provides login_manager with a method to load a user
    """
    return User.get_by_id(int(id))


@blueprint.route("/")
def index():
    """
    The public home page. Make it purty and awesome!
    """
    return jsonify({"redirect": "home"})


@blueprint.route('/login', methods=["GET", "POST"])
def login():
    """
    The all-in-one login page. Handles login logic as well as displaying the page
    :return:
    """
    # If the user is logged in, then boot them to their account

    return jsonify({
        "errors":{},
        "success": True,
        "user": g.user
    })


@blueprint.route('/logout')
def logout():
    """
    Handles logout logic
    :return:
    """
    logout_user()
    return render_template('public/logout.html')


@blueprint.route("/register", methods=['GET', 'POST'])
def register():
    """
    Handles the register logic as well as displaying the form
    :return:
    """
    register_form = RegisterForm()  # We're only getting stuff from JSON now
    if not register_form.validate():
        return jsonify({
            "errors": register_form.errors.items(),
            "success": False,
            "user": None,
            "sent_json": request.json
        })

    user = User.create(username=request.json['username'], password=request.json['password'])

    g.user = user

    return jsonify({
        "errors": [],
        "success": True,
        "user": g.user.username,
        "sent_json": request.json
    })