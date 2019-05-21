import requests
from bs4 import BeautifulSoup
url = "http://www.bloomberg.com/quote/SPX:IND"
raw_html = requests.get(url)

# get in BeautifulSoup format
processed_html = BeautifulSoup(raw_html.content, "lxml")
# print('processed_html = ', processed_html)
h1 = processed_html.findAll("h1")
print('h1 = ', h1)

