# importing libraries
from bs4 import BeautifulSoup as bs4
import urllib.request 
import urllib.parse

# variable declaration
search = input("Search : ")
title_class = "s1Q9rs"
price_class ="_30jeq3"
product=[]
price=[]

#building url
query_param=urllib.parse.quote(search)


# extraction of page's html
page=urllib.request.urlopen("https://www.flipkart.com/search?q=%s&page=1"%query_param)
html = page.read()
html= html.decode('UTF-8')

# filtering out useful elements from html
elements = bs4(html,"html.parser")

for title in elements.find_all(class_=title_class):
  product.append(title.string)

for price_ in elements.find_all(class_=price_class):
  price.append(price_.string)

# displaing the data
for i in range(0,len(product)):
  print(price[i],"::",product[i])
