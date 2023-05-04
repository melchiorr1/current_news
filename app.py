from flask import Flask, render_template, request, url_for, flash
import requests
import os


def get_articles(num=4):
    api_key = app.config['NYT_API_KEY']
    dic = {}

    response = requests.get(
        f'https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key={api_key}')
    for article in response.json()['results'][:num]:
        if article['media']:
            dic[article['title']] = [article['url'], article['media']
                                     [0]['media-metadata'][-1]['url'], article['byline']]
    return dic


app = Flask(__name__)
app.config.from_pyfile('env.py')


@app.route('/')
def index():
    return render_template("/news/index.html", articles=get_articles(16))


@app.route('/register', methods=('GET', 'POST'))
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


@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

    return render_template('/auth/login.html')


@app.route('/readlater')
def readlater():
    return render_template('/news/readlater.html')
