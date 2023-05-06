from flask import Blueprint, render_template, current_app as app, request, jsonify, flash, redirect, url_for
import requests
from flask_login import login_required, current_user
from .models import Article
from . import db
import json

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

@login_required
@bp.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        data = request.form
        title = data['title']
        url = data['url']
        authors = data['author']
        img = data['img']
        if Article.query.filter_by(title=title, user_id=current_user.id).first():
            flash("Article is already added", category='error')
            return jsonify({})

        new_article = Article(title=title, authors=authors, url=url, media=img, user_id=current_user.id)
        db.session.add(new_article)
        db.session.commit()
        flash("Article added successfully", category='success')

    return jsonify({})

@login_required
@bp.route('/delete', methods=['POST'])
def delete():
    article = json.loads(request.data)
    article_id = article['articleId']
    article = Article.query.filter_by(id=article_id, user_id=current_user.id).first()

    if article:
        print(article.title)
        db.session.delete(article)
        db.session.commit()
        flash("Article deleted successfully", category='success')
    else:
        flash("Error: You can't do that", category='error')

    return jsonify({})

