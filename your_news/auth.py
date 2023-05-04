from flask import Blueprint, render_template, request, flash
from werkzeug.security import generate_password_hash, check_password_hash

bp = Blueprint('auth', __name__)

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        repeated_password = request.form['repeat_password']
        
        if username is None:
            flash('Username is required', category='error')
        elif password is None:
            flash('Password is required', category='error')
        elif password != repeated_password:
            flash("Password don't match", category='error')
        else:
            #dodaj do bazy danych
            flash("Account created", category='success')
            pass

    return render_template('/auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

    return render_template('/auth/login.html')