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

class Color:
    CYAN      = '\033[36m'
    END       = '\033[0m'

keyword = input('search key : ')
#keyword = 'hydrothermal'
url = 'https://www.jcm.riken.jp/cgi-bin/jcm/jcm_kojin?ANY=' + keyword
parent = url.split('/')[0]+'//'+url.split('/')[2]
html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')

def call_temp(url):
    html = urllib.request.urlopen(url)
    data = BeautifulSoup(html, 'html.parser')
    text = data.get_text().splitlines()
    for inf in text:
        if 'Temperature:' in inf:
            print(url,inf)
            return inf

a = soup.find_all('a')
url_list = []

for tag in a:
    called = tag.get('href')
    if 'JCM=' in called:
        url_list.append(parent+called)
    called = tag.get('href')
    sp = tag.get('')

text = soup.get_text().splitlines()
name_list = []
for i in range(len(text)):
    if 'JCM number' in text[i]:
        name_list.append(text[i-1])

with open('output.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Speceis','JCM number','URL','Information'])
    for line in url_list:
        ind = url_list.index(line)
        print(Color.CYAN+'Calling... '+Color.END+name_list[ind])
        tmp = call_temp(line)
        writer.writerow([name_list[ind],line.split('=')[1],line,tmp])
