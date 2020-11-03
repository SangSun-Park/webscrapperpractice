import os
import csv
import requests
from bs4 import BeautifulSoup

def write_jobs(wf, isoup):
  new_info = isoup.find('div', {'id':'NormalInfo'}).find_all('tr')
  for x in new_info:
    try:
      place = x.find('td').text
      title = x.find('span', {'class':'company'}).string
      wtime = x.find('span', {'class':'time'}).string
      pay = x.find('span', {'class':'payIcon'}).string + x.find('span', {'class':'number'}).string
      wday = x.find('strong').string
      write = csv.writer(wf)
      write.writerow([place, title, wtime, pay, wday])
    except:
      continue

def make_company_file(com):
  mcom = com.find('span',{'class':'company'}).text
  com = com['href']
  brandr = requests.get(com)
  bsoup = BeautifulSoup(brandr.text, 'html.parser')
  f = open(f'{mcom}.csv', mode='+w')
  write_jobs(f, bsoup)
  f.close()

os.system("clear")
alba_url = "http://www.alba.co.kr"
r = requests.get(alba_url)
rsoup = BeautifulSoup(r.text, 'html.parser')
comp = rsoup.find('div', {'id':'MainSuperBrand'}).find_all('a', {'class':'goodsBox-info'})
for com in comp:
  make_company_file(com)