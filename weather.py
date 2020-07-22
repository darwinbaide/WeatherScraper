import sys
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import time
import pickle
from lxml import etree
import requests
import mysql1

def loadMain(site1):# loads the website in selenium and returns the data
    
    try:
        opts = Options()
        opts.headless = True # tells the script to run chrome headless
        opts.add_experimental_option('excludeSwitches', ['enable-logging'])# dont output the console errors for the webpage
        opts.binary_location = "/opt/google/chrome/chrome"
        browser = Chrome('/var/www/html/chromedriver/chromedriver',options=opts)# sets the options to the browser object
        browser.get(site1) # opens the given url
        browser.execute_script("return document.documentElement.innerHTML;")# will wait for page to load
        time.sleep(15)
        root = browser.find_element_by_xpath('/*')# find root
        text=root.get_attribute('innerHTML')# get inner html of root and whole document
        browser.quit() 
        return text
    except:
        print("Timeout.")
        return "Timeout." 


def updateCurrent():
    response = requests.get("https://www.wunderground.com/weather/us/nj/elizabeth")
    tree = etree.HTML(response.text)
    forecast=tree.xpath('/html/body/app-root/app-today/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div[1]/lib-city-current-conditions/div/div[3]/div/div[1]/p')[0].text
    rainChance=tree.xpath('/html/body/app-root/app-today/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[3]/div/lib-city-today-forecast/div/div[1]/div/div/div/a[1]')[0].text
    humidity=tree.xpath('/html/body/app-root/app-today/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[2]/div/div[1]/div[1]/lib-additional-conditions/lib-item-box/div/div[2]/div/div[5]/div[2]/lib-display-unit/span/span[1]')[0].text+"%"
    sunrise=tree.xpath('/html/body/app-root/app-today/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[2]/div/div[1]/div[2]/lib-astronomy/div/div[2]/div[2]/div[2]/span')[0].text+" am"
    sunset=tree.xpath('/html/body/app-root/app-today/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[2]/div/div[1]/div[2]/lib-astronomy/div/div[2]/div[2]/div[3]/span')[0].text+" pm"
    wind=tree.xpath('/html/body/app-root/app-today/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div[1]/lib-city-current-conditions/div/div[3]/div/div[2]/p/strong/lib-display-unit/span/span[1]')[0].text+" mph"
    high=tree.xpath('/html/body/app-root/app-today/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div[1]/lib-city-current-conditions/div/div[2]/div/div/div[1]/span[1]')[0].text
    low=tree.xpath('/html/body/app-root/app-today/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div[1]/lib-city-current-conditions/div/div[2]/div/div/div[1]/span[3]')[0].text
    current=tree.xpath('/html/body/app-root/app-today/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div[1]/lib-city-current-conditions/div/div[2]/div/div/div[2]/lib-display-unit/span/span[1]')[0].text+"°"
    print("current: "+current) 
    """     
    print("forecast: "+forecast)
    print("rain: "+rainChance)
    print("humidity: "+humidity)
    print("sunrise: "+sunrise)
    print("sunset: "+sunset)
    print("wind: "+wind)
    print("high: "+high)
    print("low: "+low)
    print("current: "+current) 
     """
        
    todayCommand="UPDATE weather.today SET forecast = '"+forecast+"',rainChance = '"+rainChance+"',humidity = '"+humidity+"',sunrise = '"+sunrise+"',sunset = '"+sunset+"',wind = '"+wind+"',high = '"+high+"',low = '"+low+"',current = '"+current+"' WHERE num = 1;"
    mysql1.runCommand(todayCommand)





def updateForecast():

    # the 10 day forecast has all the relavent data in a loaded container , so using selenium to load the page and wait a bit before returning the html
    response= loadMain("https://www.wunderground.com/forecast/us/nj/elizabeth")

    tree = etree.HTML(response)

    oneTemp=tree.xpath('/html/body/app-root/app-tenday/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div/lib-forecast-chart/div/div/div/lib-forecast-chart-header-daily/div/div/div/div[2]/a[1]/div/span[1]/span[1]')[0].text
    oneTemp=oneTemp+"/"+tree.xpath('/html/body/app-root/app-tenday/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div/lib-forecast-chart/div/div/div/lib-forecast-chart-header-daily/div/div/div/div[2]/a[1]/div/span[1]/span[3]')[0].text
    twoTemp=tree.xpath('/html/body/app-root/app-tenday/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div/lib-forecast-chart/div/div/div/lib-forecast-chart-header-daily/div/div/div/div[2]/a[2]/div/span[1]/span[1]')[0].text
    twoTemp=twoTemp+"/"+tree.xpath('/html/body/app-root/app-tenday/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div/lib-forecast-chart/div/div/div/lib-forecast-chart-header-daily/div/div/div/div[2]/a[2]/div/span[1]/span[3]')[0].text
    threeTemp=tree.xpath('/html/body/app-root/app-tenday/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div/lib-forecast-chart/div/div/div/lib-forecast-chart-header-daily/div/div/div/div[2]/a[3]/div/span[1]/span[1]')[0].text
    threeTemp=threeTemp+"/"+tree.xpath('/html/body/app-root/app-tenday/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div/lib-forecast-chart/div/div/div/lib-forecast-chart-header-daily/div/div/div/div[2]/a[3]/div/span[1]/span[3]')[0].text
    fourTemp=tree.xpath('/html/body/app-root/app-tenday/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div/lib-forecast-chart/div/div/div/lib-forecast-chart-header-daily/div/div/div/div[2]/a[4]/div/span[1]/span[1]')[0].text
    fourTemp=fourTemp+"/"+tree.xpath('/html/body/app-root/app-tenday/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div/lib-forecast-chart/div/div/div/lib-forecast-chart-header-daily/div/div/div/div[2]/a[4]/div/span[1]/span[3]')[0].text
    fiveTemp=tree.xpath('/html/body/app-root/app-tenday/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div/lib-forecast-chart/div/div/div/lib-forecast-chart-header-daily/div/div/div/div[2]/a[5]/div/span[1]/span[1]')[0].text
    fiveTemp=fiveTemp+"/"+tree.xpath('/html/body/app-root/app-tenday/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div/lib-forecast-chart/div/div/div/lib-forecast-chart-header-daily/div/div/div/div[2]/a[5]/div/span[1]/span[3]')[0].text
    sixTemp=tree.xpath('/html/body/app-root/app-tenday/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div/lib-forecast-chart/div/div/div/lib-forecast-chart-header-daily/div/div/div/div[2]/a[6]/div/span[1]/span[1]')[0].text
    sixTemp=sixTemp+"/"+tree.xpath('/html/body/app-root/app-tenday/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div/lib-forecast-chart/div/div/div/lib-forecast-chart-header-daily/div/div/div/div[2]/a[6]/div/span[1]/span[3]')[0].text

    oneDate=tree.xpath('/html/body/app-root/app-tenday/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div/lib-forecast-chart/div/div/div/lib-forecast-chart-header-daily/div/div/div/div[1]/a[1]/div/div')[0].text
    twoDate=tree.xpath('/html/body/app-root/app-tenday/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div/lib-forecast-chart/div/div/div/lib-forecast-chart-header-daily/div/div/div/div[1]/a[2]/div/div')[0].text
    threeDate=tree.xpath('/html/body/app-root/app-tenday/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div/lib-forecast-chart/div/div/div/lib-forecast-chart-header-daily/div/div/div/div[1]/a[3]/div/div')[0].text
    fourDate=tree.xpath('/html/body/app-root/app-tenday/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div/lib-forecast-chart/div/div/div/lib-forecast-chart-header-daily/div/div/div/div[1]/a[4]/div/div')[0].text
    fiveDate=tree.xpath('/html/body/app-root/app-tenday/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div/lib-forecast-chart/div/div/div/lib-forecast-chart-header-daily/div/div/div/div[1]/a[5]/div/div')[0].text
    sixDate=tree.xpath('/html/body/app-root/app-tenday/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div/lib-forecast-chart/div/div/div/lib-forecast-chart-header-daily/div/div/div/div[1]/a[6]/div/div')[0].text

    oneForecast=tree.xpath('/html/body/app-root/app-tenday/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div/lib-forecast-chart/div/div/div/lib-forecast-chart-header-daily/div/div/div/div[2]/a[1]/div/div')[0].text
    twoForecast=tree.xpath('/html/body/app-root/app-tenday/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div/lib-forecast-chart/div/div/div/lib-forecast-chart-header-daily/div/div/div/div[2]/a[2]/div/div')[0].text
    threeForecast=tree.xpath('/html/body/app-root/app-tenday/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div/lib-forecast-chart/div/div/div/lib-forecast-chart-header-daily/div/div/div/div[2]/a[3]/div/div')[0].text
    fourForecast=tree.xpath('/html/body/app-root/app-tenday/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div/lib-forecast-chart/div/div/div/lib-forecast-chart-header-daily/div/div/div/div[2]/a[4]/div/div')[0].text
    fiveForecast=tree.xpath('/html/body/app-root/app-tenday/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div/lib-forecast-chart/div/div/div/lib-forecast-chart-header-daily/div/div/div/div[2]/a[5]/div/div')[0].text
    sixForecast=tree.xpath('/html/body/app-root/app-tenday/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div/lib-forecast-chart/div/div/div/lib-forecast-chart-header-daily/div/div/div/div[2]/a[6]/div/div')[0].text

    oneChance=tree.xpath('/html/body/app-root/app-tenday/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div/lib-forecast-chart/div/div/div/lib-forecast-chart-header-daily/div/div/div/div[3]/a[1]/div/div/span')[0].text
    twoChance=tree.xpath('/html/body/app-root/app-tenday/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div/lib-forecast-chart/div/div/div/lib-forecast-chart-header-daily/div/div/div/div[3]/a[2]/div/div/span')[0].text
    threeChance=tree.xpath('/html/body/app-root/app-tenday/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div/lib-forecast-chart/div/div/div/lib-forecast-chart-header-daily/div/div/div/div[3]/a[3]/div/div/span')[0].text
    fourChance=tree.xpath('/html/body/app-root/app-tenday/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div/lib-forecast-chart/div/div/div/lib-forecast-chart-header-daily/div/div/div/div[3]/a[4]/div/div/span')[0].text
    fiveChance=tree.xpath('/html/body/app-root/app-tenday/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div/lib-forecast-chart/div/div/div/lib-forecast-chart-header-daily/div/div/div/div[3]/a[5]/div/div/span')[0].text
    sixChance=tree.xpath('/html/body/app-root/app-tenday/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div/lib-forecast-chart/div/div/div/lib-forecast-chart-header-daily/div/div/div/div[3]/a[6]/div/div/span')[0].text
    """ 
    print("1----temp:"+oneTemp)
    print("1----date:"+oneDate)
    print("1----forecast:"+oneForecast)
    print("1----chance:"+oneChance)

    print("2----temp:"+twoTemp)
    print("2----date:"+twoDate)
    print("2----forecast:"+twoForecast)
    print("2----chance:"+twoChance)

    print("3----temp:"+threeTemp)
    print("3----date:"+threeDate)
    print("3----forecast:"+threeForecast)
    print("3----chance:"+threeChance)

    print("4----temp:"+fourTemp)
    print("4----date:"+fourDate)
    print("4----forecast:"+fourForecast)
    print("4----chance:"+fourChance)

    print("5----temp:"+fiveTemp)
    print("5----date:"+fiveDate)
    print("5----forecast:"+fiveForecast)
    print("5----chance:"+fiveChance)

    print("6----temp:"+sixTemp)
    print("6----date:"+sixDate)
    print("6----forecast:"+sixForecast)
    print("6----chance:"+sixChance)
    """

    forecastCommand="UPDATE forecast SET oneDate = '"+oneDate+"',oneTemp = '"+oneTemp+"',oneForecast = '"+oneForecast+"',oneChance = '"+oneChance+"',twoDate = '"+twoDate+"',twoTemp = '"+twoTemp+"',twoForecast = '"+twoForecast+"',twoChance = '"+twoChance+"',threeDate = '"+threeDate+"',threeTemp = '"+threeTemp+"',threeForecast = '"+threeForecast+"',threeChance = '"+threeChance+"',fourDate = '"+fourDate+"',fourTemp = '"+fourTemp+"',fourForecast = '"+fourForecast+"',fourChance = '"+fourChance+"',fiveDate = '"+fiveDate+"',fiveTemp = '"+fiveTemp+"',fiveForecast = '"+fiveForecast+"',fiveChance = '"+fiveChance+"',sixDate = '"+sixDate+"',sixTemp = '"+sixTemp+"',sixForecast = '"+sixForecast+"',sixChance = '"+sixChance+"'  ,timestamp = now() WHERE num = 0;"
    mysql1.runCommand(forecastCommand)




def main():
    count=0
    while True:# run forever
        print("Start of session")
        try:
            updateCurrent()# run everytime
            print("Ran current updater")
        except:
            print("Error in updating current")
        
        if(count>7):# every 8 passes it will update the forecast as that doesnt change as often
            try:
                updateForecast()
                print("Ran forecast updater")
                count=0# resets counter to zero to count again
            except:
                print("Error in updating forecast")
        else:
            count=count+1# if not yet 8 then increment
        print("End of Session, Sleeping for thirty minutes")
        time.sleep(1800)# 30 minutes

main()


