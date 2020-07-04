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
#wind=wind+" "+tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[1]/div/ul/li[1]/div/span[2]')[0].text

high=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[1]/summary/div/div/div[1]/span[1]')[0].text
low=tree.xpath('//html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[1]/summary/div/div/div[1]/span[2]/span')[0].text
current=tree.xpath('/html/body/div[1]/div[3]/div[2]/div/div/div/div[1]/div/div/div/a[1]/span')[0].text








oneTemp=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[2]/summary/div/div/div[1]/span[1]')[0].text
oneTemp=oneTemp+"/"+tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[2]/summary/div/div/div[1]/span[2]/span')[0].text
twoTemp=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[3]/summary/div/div/div[1]/span[1]')[0].text
twoTemp=twoTemp+"/"+tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[3]/summary/div/div/div[1]/span[2]/span')[0].text
threeTemp=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[4]/summary/div/div/div[1]/span[1]')[0].text
threeTemp=threeTemp+"/"+tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[4]/summary/div/div/div[1]/span[2]/span')[0].text
fourTemp=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[5]/summary/div/div/div[1]/span[1]')[0].text
fourTemp=fourTemp+"/"+tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[5]/summary/div/div/div[1]/span[2]/span')[0].text
fiveTemp=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[6]/summary/div/div/div[1]/span[1]')[0].text
fiveTemp=fiveTemp+"/"+tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[6]/summary/div/div/div[1]/span[2]/span')[0].text
sixTemp=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[7]/summary/div/div/div[1]/span[1]')[0].text
sixTemp=sixTemp+"/"+tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[7]/summary/div/div/div[1]/span[2]/span')[0].text


oneDate=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[2]/summary/div/div/h3')[0].text
twoDate=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[3]/summary/div/div/h3')[0].text
threeDate=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[4]/summary/div/div/h3')[0].text
fourDate=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[5]/summary/div/div/h3')[0].text
fiveDate=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[6]/summary/div/div/h3')[0].text
sixDate=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[7]/summary/div/div/h3')[0].text


oneForecast=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[2]/summary/div/div/div[2]/span')[0].text
twoForecast=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[3]/summary/div/div/div[2]/span')[0].text
threeForecast=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[4]/summary/div/div/div[2]/span')[0].text
fourForecast=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[5]/summary/div/div/div[2]/span')[0].text
fiveForecast=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[6]/summary/div/div/div[2]/span')[0].text
sixForecast=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[7]/summary/div/div/div[2]/span')[0].text



oneChance=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[2]/summary/div/div/div[3]/span')[0].text
twoChance=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[3]/summary/div/div/div[3]/span')[0].text
threeChance=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[4]/summary/div/div/div[3]/span')[0].text
fourChance=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[5]/summary/div/div/div[3]/span')[0].text
fiveChance=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[6]/summary/div/div/div[3]/span')[0].text
sixChance=tree.xpath('/html/body/div[1]/div[6]/main/div[1]/section/div[2]/details[7]/summary/div/div/div[3]/span')[0].text



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




print("forecast: "+forecast)
print("rain: "+rainChance)
print("humidity: "+humidity)
print("sunrise: "+sunrise)
print("sunset: "+sunset)
print("wind: "+wind)
print("high: "+high)
print("low: "+low)
print("current: "+current) 

forecastCommand="UPDATE forecast SET oneDate = '"+oneDate+"',oneTemp = '"+oneTemp+"',oneForecast = '"+oneForecast+"',oneChance = '"+oneChance+"',twoDate = '"+twoDate+"',twoTemp = '"+twoTemp+"',twoForecast = '"+twoForecast+"',twoChance = '"+twoChance+"',threeDate = '"+threeDate+"',threeTemp = '"+threeTemp+"',threeForecast = '"+threeForecast+"',threeChance = '"+threeChance+"',fourDate = '"+fourDate+"',fourTemp = '"+fourTemp+"',fourForecast = '"+fourForecast+"',fourChance = '"+fourChance+"',fiveDate = '"+fiveDate+"',fiveTemp = '"+fiveTemp+"',fiveForecast = '"+fiveForecast+"',fiveChance = '"+fiveChance+"',sixDate = '"+sixDate+"',sixTemp = '"+sixTemp+"',sixForecast = '"+sixForecast+"',sixChance = '"+sixChance+"'  ,timestamp = now() WHERE num = 0;"




#forecastCommand="UPDATE 'weather'.'forecast'SET 'oneDate' = "+oneDate+",'oneTemp' = "+oneTemp+",'oneForecast' = "+oneForecast+",'oneChance' = "+oneChance+",'twoDate' = "+twoDate+",'twoTemp' = "+twoTemp+",'twoForecast' = "+twoForecast+",'twoChance' = "+twoChance+",'threeDate' = "+threeDate+",'threeTemp' = "+threeTemp+",'threeForecast' = "+threeForecast+",'threeChance' = "+threeChance+",'fourDate' = "+fourDate+",'fourTemp' = "+fourTemp+",'fourForecast' = "+fourForecast+",'fourChance' = "+fourChance+",'fiveDate' = "+fiveDate+",'fiveTemp' = "+fiveTemp+",'fiveForecast' = "+fiveForecast+",'fiveChance' = "+fiveChance+",'sixDate' = "+sixDate+",'sixTemp' = "+sixTemp+",'sixForecast' = "+sixForecast+",'sixChance' = "+sixChance+"  ,'timestamp' = now()  WHERE 'index' = 0;"


todayCommand="UPDATE weather.today SET forecast = '"+forecast+"',rainChance = '"+rainChance+"',humidity = '"+humidity+"',sunrise = '"+sunrise+"',sunset = '"+sunset+"',wind = '"+wind+"',high = '"+high+"',low = '"+low+"',current = '"+current+"' WHERE num = 1;"




#print(forecastCommand)
#print(todayCommand)
mysql1.runCommand(todayCommand)
mysql1.runCommand(forecastCommand)