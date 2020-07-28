import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options


def loadMain():
        
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome('/var/www/html/darwin/WeatherScraper/chromedriver',options=chrome_options)

    #driver = Chrome(executable_path="/var/www/html/darwin/WeatherScraper/chromedriver",chrome_options=chrome_options)  # Optional argument, if not specified will search path.
    driver.get('https://www.wunderground.com/weather/us/nj/elizabeth')

    root = driver.find_element_by_xpath('/*')# find root
    text=root.get_attribute('innerHTML')# get inner html of root and whole document
    driver.quit() 
    print(text)
    #driver.quit()