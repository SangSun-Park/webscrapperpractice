import requests
from flask import Flask, render_template, request
from bs4 import BeautifulSoup
"""
When you try to scrape reddit make sure to send the 'headers' on your request.
Reddit blocks scrappers so we have to include these headers to make reddit think
that we are a normal computer and not a python script.
How to use: requests.get(url, headers=headers)
"""

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


"""
All subreddits have the same url:
i.e : https://reddit.com/r/javascript
You can add more subreddits to the list, just make sure they exist.
To make a request, use this url:
https://www.reddit.com/r/{subreddit}/top/?t=month
This will give you the top posts in per month.
"""

subreddits = [
    "javascript",
    "reactjs",
    "reactnative",
    "programming",
    "css",
    "golang",
    "flutter",
    "rust",
    "django"
]

app = Flask("DayEleven")

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/read')
def read():
  reading = []
  reads_list = []
  for sub in subreddits:
    aggrement = request.args.get(sub)
    if aggrement:
      reading.append(sub)
      url = f'https://www.reddit.com/r/{sub}/top/?t=month'
      req = requests.get(url, headers=headers)
      req_soup = BeautifulSoup(req.text, 'html.parser').find_all('div', {'class':'_1oQyIsiPHYt6nx7VOmd1sz'})
      for re in req_soup:
        try:
          dic = []
          title = re.find('h3', {'class':'_eYtD2XCVieq6emjKBH3m'}).string
          title_url = re.find('a', {'class', 'SQnoC3ObvgnGjWt90zD9Z'})['href']
          point = re.find('div', {'class':'_1rZYMD_4xY3gRcSS3p8ODO'}).string
          if 'k' in point:
            point.replace('k','')
            point = int(point) * 1000
          dic.append(title)
          dic.append(title_url)
          dic.append(point)
          dic.append('r/'+sub)
          reads_list.append(dic)
        except:
          continue
  return render_template('read.html', reads=reading, reads_lists = reads_list)

app.run(host="0.0.0.0")