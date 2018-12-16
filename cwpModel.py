import json
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pprint import pprint

CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = './lib/chromedriver'

with open('input.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

print('Number of web pages:',len(data['params']))

chrome_options = Options()
chrome_options.binary_location = CHROME_PATH
chrome_options.add_argument('--headless')

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,chrome_options=chrome_options)
for record in data['params']:
    print('Processing page: ' + record['url'])
    for resolution in record['resolutions']:
        driver.get(record['url'])
        w,h = resolution.split(',')
        driver.set_window_size(w, h, driver.window_handles[0])
        filename = '/mnt/c/Users/Pawel/Pictures/'+record['url'].replace('https://','').replace('http://','')+'_'+resolution.replace(',','_')+'.png'
        print(filename)
        driver.save_screenshot(filename)
driver.close()
