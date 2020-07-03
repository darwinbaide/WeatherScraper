from lxml import etree
import requests

response = requests.get("https://www.wunderground.com/weather/us/nj/elizabeth/KNJELIZA13")
tree = etree.HTML(response.text)

temp=tree.xpath('/html/body/app-root/app-today/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div[1]/lib-city-current-conditions/div/div[2]/div/div/div[2]/lib-display-unit/span/span[1]')[0]
forecast=tree.xpath('/html/body/app-root/app-today/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div[1]/lib-city-current-conditions/div/div[3]/div/div[1]/p')[0]
wind=tree.xpath('/html/body/app-root/app-today/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div[1]/lib-city-current-conditions/div/div[3]/div/div[2]/p/strong/lib-display-unit/span/span[1]')[0]
prec=tree.xpath('/html/body/app-root/app-today/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[3]/div/lib-city-today-forecast/div/div[2]/div/div/div/a[1]')[0]
high=tree.xpath('/html/body/app-root/app-today/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[3]/div/lib-city-today-forecast/div/div[1]/div/a/div/div[2]/span[3]/span/lib-display-unit/span/span[1]')[0]
low=tree.xpath('/html/body/app-root/app-today/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[3]/div/lib-city-today-forecast/div/div[2]/div/a/div/div[2]/span[3]/span/lib-display-unit/span/span[1]')[0]
thigh=tree.xpath('/html/body/app-root/app-today/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[3]/div/lib-city-today-forecast/div/div[3]/div/a/div/div[2]/span[3]/span[1]/lib-display-unit/span/span[1]')[0]
tlow=tree.xpath('/html/body/app-root/app-today/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[3]/div/lib-city-today-forecast/div/div[3]/div/a/div/div[2]/span[3]/span[2]/lib-display-unit/span/span[1]')[0]
img=tree.xpath('/html/body/app-root/app-today/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[1]/div[1]/lib-city-current-conditions/div/div[3]/div/div[1]/img')[0]
timg=tree.xpath('/html/body/app-root/app-today/one-column-layout/wu-header/sidenav/mat-sidenav-container/mat-sidenav-content/div/section/div[3]/div[1]/div/div[3]/div/lib-city-today-forecast/div/div[3]/div/a/div/div[1]/img')[0]

print("Temp: "+temp.text)
print("Forecast: "+forecast.text)
print("Wind: "+wind.text)
print("Precipitation: "+prec.text.split(" ")[0])
print("High Temp: "+high.text)
print("Low Temp: "+low.text)
print("Img: "+img.attrib['src'])
print("Tomorrow High Temp: "+thigh.text)
print("Tommorrow Low Temp: "+tlow.text)
print("Tommorrow Img: "+timg.attrib['src'])