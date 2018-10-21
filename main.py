from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv
#from index import go

TitleStorage = open('articleTitles.txt', 'w')
URLStorage = open('articleURLS.txt', 'w')
DateStorage = open('articleDates.txt', 'w')
Publication = open('publication.txt','w')

def run():
    # CONNECT TO ALJAZEERA WEB PAGE
    url = urlopen("https://www.aljazeera.com/news")
    # GRAB HTML TAGS
    bsObj = BeautifulSoup(url, features="html.parser")

    # MAIN ARITCLE SCRAPE
    bigTitle = bsObj.findAll("h2", {"class": "top-sec-title"})
    bigLink = bsObj.find("div", {"class": "top-feature-overlay-cont"})

    # ITERATE OVER TAGS AND GRAB ARTICLE TITLES
    for article in bigTitle:
        heading_data = article.text
        TitleStorage.write(heading_data + '\n')

    URLList = []
    possible_links = bigLink.find_all('a')
    for url in possible_links:
        if url.has_attr('href'):
            URLList.append("https://www.aljazeera.com"+url.attrs['href'])

    smalltitle = bsObj.findAll("h2", {"class": "top-sec-smalltitle"})

    for article in smalltitle:
        heading_data = article.text
        TitleStorage.write(heading_data)
        TitleStorage.write("\n")

    smallLink = bsObj.find("div", {"class": "col-md-6 middle-east-bot"})
    i = 0
    possible_links = smallLink.find_all('a')
    for url in possible_links:
        if url.has_attr('href'):
            if i==0 or i==3 or i==6 or i==11:
                URLList.append("https://www.aljazeera.com"+ url.attrs['href'])
            i = i + 1

    for i in range(1, len(URLList)):
        URLStorage.write(URLList[i] + "\n")

    NewsList=["aljazeera","abcnews","cnn"]
    for i in range(1,len(URLList)):
        for j in range(0,len(NewsList)):
            if NewsList[j] in URLList[i]:
                 Publication.write(NewsList[j] + "\n")

run()
