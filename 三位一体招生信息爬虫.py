# -*- coding: utf-8 -*-

import requests, bs4, ssl, re

res = requests.get('http://www.eol.cn/html/g/zjswyt/')
res.encoding = 'utf8'
res.raise_for_status()

# Passes the `text` attribute of the response to `bs4.BeautifulSoup()`.
# The ` BeautifualSoup` object that it returns is stored in a variable named `soup`
soup = bs4.BeautifulSoup(res.text, features="html5lib")

# Retrieve the elemente that use a CSS class attribute named willnum-body from the BeautifulSoap object
raw_form = soup.select('.willnum-body > table > tbody > tr > td')

print(raw_form)
