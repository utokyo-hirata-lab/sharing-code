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

#keyword = input('search key : ')
keyword = 'hydrothermal'
url = 'https://www.jcm.riken.jp/cgi-bin/jcm/jcm_kojin?ANY=' + keyword
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

a = soup.find_all("a")
#for script in soup(["script", "style"]):
#    script.decompose()
for tag in a:
    called = 
    if 'JCM=' in tag.get('href'):
        print(tag.get('href'))
