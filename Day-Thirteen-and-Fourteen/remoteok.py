import requests
from bs4 import BeautifulSoup

remoteok_url = "https://remoteok.io"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}


def find_jobs(job_lists, word):
  url = f"https://remoteok.io/remote-{word}-jobs"
  job = requests.get(url, headers= headers)
  job_soup = BeautifulSoup(job.text, 'html.parser')
  return extrate(job_lists, url, job_soup)

def extrate(job_lists, url, soup):
  job_soup = soup.find_all('tr', {'class':'job'})
  for jobs in job_soup:
    job_list = []
    try:
      title = jobs.find('h2', {'itemprop':'title'}).string
      links = jobs.find('a', {'itemprop':'url'})['href']
      company = jobs.find('h3', {'itemprop':'name'}).string
      job_list.append(title)
      job_list.append(company)
      job_list.append(remoteok_url+links)
      job_lists.append(job_list)
    except:
      continue
  return  job_lists 
