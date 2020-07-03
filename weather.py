from lxml import etree
import requests
import mysql1

response = requests.get("https://weather.com/weather/tenday/l/e8192ee9d5dea16026ba122310f729292c86526268b64e712bdc275141861928")

tree = etree.HTML(response.text)

forecast=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[1]/summary/div/div/div[2]/span')[0].text
rainChance=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[1]/summary/div/div/div[3]/span')[0].text
humidity=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[1]/div/ul[1]/li[3]/div/span[2]')[0].text
sunrise=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[1]/div/ul[1]/li[5]/div/span[2]')[0].text
sunset=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[1]/div/ul[1]/li[6]/div/span[2]')[0].text
wind=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[1]/div/ul[1]/li[1]/div/span[2]')[0].text
high=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[1]/summary/div/div/div[1]/span[1]')[0].text
low=tree.xpath('//html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[1]/summary/div/div/div[1]/span[2]/span')[0].text
current=tree.xpath('/html/body/div[1]/div[3]/div[2]/div/div/div/div[1]/div/div/div/a[1]/span')[0].text



print("forecast: "+forecast)
print("rain: "+rainChance)
print("humidity: "+humidity)
print("sunrise: "+sunrise)
print("sunset: "+sunset)
print("wind: "+wind)
print("high: "+high)
print("low: "+low)
print("current: "+current)

insertCommand="INSERT INTO `weather`.`today`(`forecast`,`rainChance`,`humidity`,`sunrise`,`sunset`,`wind`,`high`,`low`,`current`) VALUES("+forecast+","+rainChance+","+humidity+","+sunrise+","+sunset+","+wind+","+high+","+low+","+current+");"
command="SELECT * FROM weather.today;"
mysql1.runCommand(command)