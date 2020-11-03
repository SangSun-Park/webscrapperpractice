"""
These are the URLs that will give you remote jobs for the word 'python'

https://stackoverflow.com/jobs?r=true&q=python
https://weworkremotely.com/remote-jobs/search?term=python
https://remoteok.io/remote-python-jobs

Good luck!
"""
from flask import Flask, render_template, request, redirect, send_file
import stack, remoteok, wwr, save

jobDB = {}

app = Flask("scrapper")

@app.route('/')
def hoem():
  return render_template('home.html')

@app.route('/search')
def search():
  word = request.args.get('term').lower()
  lists = []
  if not jobDB.get(word):
    lists = wwr.find_jobs(lists, word)
    stack.find_jobs(lists, word)
    remoteok.find_jobs(lists, word)
    jobDB[word] = lists
  else:
    lists = jobDB.get(word)
  return render_template('search.html', serchingjobs = len(lists), jobs = lists, searchingBy = word)

@app.route('/export')
def export():
  try:
    word = request.args.get('term')
    if not word:
      raise Exception()
    word = word.lower()
    jobs = jobDB.get(word)
    if not jobs:
      raise Exception()
    save.save_to_file(jobs, word)
    return send_file(f'{word}.csv', as_attachment=True, attachment_filename=f'{word}.csv')
  except:
    return redirect('/')

app.run(host='0.0.0.0')