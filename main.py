from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

article_file = open('day1.txt','w')

def run():
    # CONNECT TO ALJAZEERA WEB PAGE
    url = urlopen("https://www.aljazeera.com/news")
    # GRAB HTML TAGS
    bsObj = BeautifulSoup(url, features="html.parser")
    bigtitle = bsObj.findAll("h2", {"class": "top-sec-title"})
    smalltitle = bsObj.findAll("h2", {"class": "top-sec-smalltitle"})

    # ITERATE OVER TAGS AND GRAB ARTICLE TITLES
    i = 0
    for article in bigtitle:
        heading_data = article.text
        print(heading_data)

        article_file.write(heading_data)
        article_file.write('\n')

        i = i + 1

    m = 0
    for article in smalltitle:
        heading_data = article.text
        print(heading_data)

        article_file.write(heading_data)
        article_file.write("\n")

        m = m + 1

run()