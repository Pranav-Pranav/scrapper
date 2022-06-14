# importing libraries
from bs4 import BeautifulSoup as bs4
import urllib.request 
import urllib.parse

search = input("Search : ")
title_class = "s1Q9rs"
price_class ="_30jeq3"
product=[]
price=[]

query_param=urllib.parse.quote(search)
def end():
  print("xxxxxxxxxxxxxxxxxxx end of search xxxxxxxxxxxxxxxxxxx")
 
def main(query_param,title_class,price_class,product,price,page_no):
  page=urllib.request.urlopen("https://www.flipkart.com/search?q=%s&page=%s"%(query_param,page_no))
  html = page.read()
  html= html.decode('UTF-8')

  # filtering out useful elements from html
  elements = bs4(html,"html.parser")

  for title in elements.find_all(class_=title_class):
    product.append(title.string)

  for price_ in elements.find_all(class_=price_class):
    price.append(price_.string)

  # displaing the data
  print("========================== Page No. %s =========================="%page_no)
  print("\n\n")
  for i in range(0,len(product)):
    print(price[i],"::",product[i])

  if len(product)>0:
    print("\n\n")
    main(query_param,title_class,price_class,product,price,page_no+1)
  else :
    end()  


main(query_param,title_class,price_class,product,price,1)
