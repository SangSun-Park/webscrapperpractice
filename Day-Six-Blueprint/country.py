import requests
from bs4 import BeautifulSoup

def find(country):
  try:
    print('Input the country nuber : ', end='')
    cnum = int(input())
    if cnum in country:
      coun = country[cnum]
      print(coun[0])
      return coun[2]
    else:
      print(f'{cnum} is not in Country Numbers try again')
      find(country)
  except:
    print('It is not number!')
    find(country)

def country_print(country):
  for c in country:
    print(f'#{c} {country[c][0]}')

def country_set():
  country = {}
  url = "https://www.iban.com/currency-codes"
  r = requests.get(url)
  soup = BeautifulSoup(r.text, 'html.parser')
  x_soup = soup.find('table', {'class':'table table-bordered downloads tablesorter'})
  x = x_soup.find_all('tr')
  j = 0
  for i in x[1:]:
    i = i.find_all('td')
    if i[1].string != 'No universal currency':
      country[j] = [i[0].string, i[1].string, i[2].string, i[3].string]
      j += 1
  return country

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
