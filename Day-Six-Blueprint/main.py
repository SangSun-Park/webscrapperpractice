import os
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency
import country

os.system("clear")

"""
Use the 'format_currency' function to format the output of the conversion
format_currency(AMOUNT, CURRENCY_CODE, locale="ko_KR" (no need to change this one))
"""

def check_num():
  print(f'How many {cfrom} do you want to convert to {cto}?')
  try:
    change_money = int(input())
    return change_money
  except:
    print('Input number!')
    return check_num()

countrys = country.country_set()
country.country_print(countrys)
print('\n\n\n')
cfrom = country.find(countrys)
cto = country.find(countrys)
mch = check_num()
urls = f"https://transferwise.com/gb/currency-converter/{cfrom}-to-{cto}-rate?amount={mch}"
r = requests.get(urls)
soup = BeautifulSoup(r.text, 'html.parser')
amou = float(soup.find('div', {'class':'col-lg-6 text-xs-center text-lg-left'}).find('span',{'class':'text-success'}).string.encode('utf-8').decode('utf-8'))
print(f'{cfrom} {mch} is '+format_currency(mch*amou, cto, locale="ko_KR"))