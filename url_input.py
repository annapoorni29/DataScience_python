import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
url=input("Enter url: ")
html = urllib.request.urlopen(url)
parser = BeautifulSoup(html, 'html.parser')
print(parser)
tags = parser('a')
for tag in tags:
    print(tag.get("href", None))