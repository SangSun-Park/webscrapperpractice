import requests
from bs4 import BeautifulSoup

wwr_url = "https://weworkremotely.com"

def find_jobs(job_lists, word):
  url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
  job = requests.get(url)
  job_soup = BeautifulSoup(job.text, 'html.parser')
  return extrate(job_lists, url, job_soup)

def extrate(job_lists, url, soup):
  job_soup = soup.find_all('li', {'class':'feature'})
  for jobs in job_soup:
    job_list = []
    try:
      jobs = jobs.find('a')
      title = jobs.find('span', {'class':'title'}).string
      links = jobs['href']
      company = jobs.find('span', {'class':'company'}).string
      job_list.append(title)
      job_list.append(company)
      job_list.append(wwr_url+links)
      job_lists.append(job_list)
    except:
      continue
  return  job_lists 
