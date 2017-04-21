#!/usr/bin/python
#from sys import argv
import sys
from HTMLParser import HTMLParser
import requests
package_repository_url = sys.argv[1]
package_name = sys.argv[2]
result = requests.get(package_repository_url).text
temp = []
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name, value in attrs:
                if name == "href":
                    temp.append(value)
parser = MyHTMLParser()
parser.feed(result)
for idx, word in enumerate(temp):
    if package_name in word:
        print word
