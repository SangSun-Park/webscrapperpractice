import os
import requests
from bs4 import BeautifulSoup

country = {}

def find():
  try:
    print('Input the country nuber : ', end='')
    cnum = input()
    int(cnum)
    if cnum in country:
      coun = country[cnum]
      print(f"Name : {coun[0]}, Currency Code : {coun[2]}")
    else:
      print(f'{cnum} is not in Country Numbers try again')
      find()
  except:
    print('It is not number!')
    find()

def country_set():
  url = "https://www.iban.com/currency-codes"
  r = requests.get(url)
  soup = BeautifulSoup(r.text, 'html.parser')
  x_soup = soup.find('table', {'class':'table table-bordered downloads tablesorter'})
  x = x_soup.find_all('tr')
  for i in x[1:]:
    i = i.find_all('td')
    if i[1].string != 'No universal currency':
      country[i[3].string] = [i[0].string, i[1].string, i[2].string, i[3].string]

def bye():
  print('Do you want find other Country? y/n : ', end='')
  find_again = input().lower()
  if find_again == 'y':
    return True
  elif find_again == 'n':
    print('ok, bye!')
    return False
  else:
    print('wrong input')
    return bye()

country_set()
x = True
while x:
  os.system('clear')
  find()
  x = bye()