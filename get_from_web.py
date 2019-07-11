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

keyword = input('search key : ') #キーワードを入力する
#keyword = 'hydrothermal' 
url = 'https://www.jcm.riken.jp/cgi-bin/jcm/jcm_kojin?ANY=' + keyword #URLをつくる
html = urllib.request.urlopen(url) #URLからhtmlを取得する 
soup = BeautifulSoup(html, 'html.parser') 

a = soup.find_all("a") #aタグ(urlが含まれる)のリストを取得
#for script in soup(["script", "style"]):
#    script.decompose()
for tag in a:
    if 'JCM=' in tag.get('href'): #URLにJCM=が含まれるものを取得
        print(tag.get('href'))
