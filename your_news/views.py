from flask import Blueprint, render_template, current_app as app
import requests
from flask_login import login_required, current_user


bp = Blueprint('views', __name__)

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

@bp.route('/')
def index():
    return render_template("/news/index.html", articles=get_articles(16), user=current_user)

@bp.route('/readlater')
@login_required
def readlater():
    return render_template('/news/readlater.html', user=current_user)