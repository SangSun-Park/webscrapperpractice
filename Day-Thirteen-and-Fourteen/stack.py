import requests
from bs4 import BeautifulSoup

stackoverflow_url = "https://stackoverflow.com"

def find_jobs(job_lists, word):
  url = f"https://stackoverflow.com/jobs?r=true&q={word}"
  job = requests.get(url)
  job_soup = BeautifulSoup(job.text, 'html.parser')
  return extrate(job_lists, url, job_soup)

def extrate(job_lists, url, soup):
  pages = find_pagination(soup)
  for page in pages:
    page = page.find('span').string
    urls = url + f'&pg={page}'
    page_job = requests.get(urls)
    page_jsoup = BeautifulSoup(page_job.text, 'html.parser').find_all('div', {'class':'grid'})
    for jobs in page_jsoup:
      job_list = []
      try:
        title = jobs.find('a', {'class':'s-link stretched-link'})['title']
        links = jobs.find('a', {'class':'s-link stretched-link'})['href']
        company = jobs.find('h3', {'class':'fc-black-700'}).find('span').string
        job_list.append(title)
        job_list.append(company)
        job_list.append(stackoverflow_url+links)
        job_lists.append(job_list)
      except:
        continue
  return  job_lists 

def find_pagination(soup):
  paginations = soup.find_all('a', {'class':'s-pagination--item'})
  return paginations[:-1]