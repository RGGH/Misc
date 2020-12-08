# bs4

from bs4 import BeautifulSoup
import requests

my_page = "Wohnung mieten im Umkreis von 50 km von Mannheim - ImmobilienScout24.html"

soup = BeautifulSoup(open(my_page),"lxml")
soup = soup.find('div',class_ = "select-input-wrapper")
items = soup.select('option[value]')
values = [item.get('value') for item in items]
x = [int(item) for item in values]
print(x)


########

# scrapy:

fetch('https:zoopla.co.uk')
response.xpath('//select/option/text()').getall() # gets all dropdown values
response.xpath('//select[@id="forsale_price_max"]/option/text()').getall()
