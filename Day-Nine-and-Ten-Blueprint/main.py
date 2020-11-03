import requests, html
from flask import Flask, render_template, request, redirect
from bs4 import BeautifulSoup

base_url = "http://hn.algolia.com/api/v1"

# This URL gets the newest stories.
new = f"{base_url}/search_by_date?tags=story"

# This URL gets the most popular stories
popular = f"{base_url}/search?tags=story"

cDB = {}


# This function makes the URL to get the detail of a storie by id.
# Heres the documentation: https://hn.algolia.com/api
def make_detail_url(id):
    return f"{base_url}/items/{id}"


app = Flask("DayNine")

def find_child(x, texts = ''):
  if x['text']:
    texts += str(BeautifulSoup(html.unescape(x['text']), 'html.parser').find('p'))
  if x['children']:
    texts = find_child(x['children'], texts)
  return texts

@app.route('/')
def defa():
    order_by = request.args.get('order_by')
    m = 1
    if order_by == 'new':
      news_page = requests.get(new).json()
      m = 2
    else :
      news_page = requests.get(popular).json()
    return render_template("main.html", mode=m, news=news_page)


@app.route('/?order_by=popular')
def popular_news():
    populars = requests.get(popular).json()
    return render_template("main.html", mode=1, news=populars)


@app.route('/?order_by=new')
def new_news():
    newest = requests.get(new).json()
    return render_template("main.html", mode=2, news=newest)


@app.route('/<id>')
def comment(id):
  try:
    if id not in cDB:
        cDB[str(id)] = requests.get(make_detail_url(id)).json()
        for x in cDB[str(id)]['children']:
            if x['text']:
                x['text'] = find_child(x)
    return render_template('index.html', com=cDB[str(id)])
  except:
    return redirect('/')


app.run(host="0.0.0.0")
