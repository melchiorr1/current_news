from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import requests
import os

def get_articles():
    api_key = app.config['NYT_API_KEY']
    dic = {}

    response = requests.get(f'https://api.nytimes.com/svc/mostpopular/v2/viewed/1.json?api-key={api_key}')
    for article in response.json()['results'][:4]:
        dic[article['title']] = article['media'][0]['media-metadata'][-1]['url']
    return dic

app = Flask(__name__)
app.config.from_pyfile('.env.py')

@app.route('/')
def index():
    return render_template("index.html", articles=get_articles())

