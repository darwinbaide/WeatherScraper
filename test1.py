import sys
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
import time
import pickle
from lxml import etree
import requests
import mysql1

site1="https://www.wunderground.com/weather/us/nj/elizabeth"



opts = Options()
opts.headless = True # tells the script to run chrome headless
opts.add_experimental_option('excludeSwitches', ['enable-logging'])# dont output the console errors for the webpage
#driver = webdriver.Chrome('chromedriver.exe') 
browser = Chrome('chromedriver.exe',options=opts)# sets the options to the browser object
browser.get(site1) # opens the given url
browser.execute_script("return document.documentElement.innerHTML;")# will wait for page to load
#time.sleep(15)
root = browser.find_element_by_xpath('/*')# find root
text=root.get_attribute('innerHTML')# get inner html of root and whole document
browser.quit() 
print(text)