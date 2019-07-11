from selenium import webdriver
import time
import requests
import json
from bs4 import BeautifulSoup
import pandas as pd
import sys
import time
import os
import urllib
import csv
import pprint

#keyword = input('search key : ')
keyword = 'hydrothermal'
url = 'https://www.jcm.riken.jp/cgi-bin/jcm/jcm_kojin?ANY=' + keyword
parent = url.split('/')[0]+'//'+url.split('/')[2]
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

a = soup.find_all("a")
#for script in soup(["script", "style"]):
#    script.decompose()
url_list = []
for tag in a:
    called = tag.get('href')
    if 'JCM=' in called:
        url_list.append(parent+called)
print(len(url_list))
with open('output.csv', 'w') as f:
    writer = csv.writer(f)
    for line in url_list:
        writer.writerow([line.split('=')[1],line])
