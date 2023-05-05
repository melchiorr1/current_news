from flask import Blueprint, render_template, request, flash, redirect,  url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user

bp = Blueprint('auth', __name__)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('views.index'))

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        repeated_password = request.form['repeat_password']
        user = User.query.filter_by(email=email).first()
        if username is None:
            flash('Username is required', category='error')
        elif user:
            flash('Email is already used', category='error')
        elif password is None:
            flash('Password is required', category='error')
        elif password != repeated_password:
            flash("Password don't match", category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash("Account created", category='success')
            return redirect(url_for('views.index'))

    return render_template('/auth/register.html', user=current_user)


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        user = User.query.filter_by(email=email).first()
        if user: 
            if check_password_hash(user.password, password):
                flash('Logged in sucessfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.index'))
            else:
                flash("Incorrect password", category='error')
        else:
            flash('Email does not exists', category='error')


    return render_template('/auth/login.html', user=current_user)