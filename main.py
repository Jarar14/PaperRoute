from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

infoStorage = open('day1.txt', 'w')


def run():
    # CONNECT TO ALJAZEERA WEB PAGE
    url = urlopen("https://www.aljazeera.com/news")
    # GRAB HTML TAGS
    bsObj = BeautifulSoup(url, features="html.parser")


    # MAIN ARITCLE SCRAPE
    bigTitle = bsObj.findAll("h2", {"class": "top-sec-title"})
    bigLink = bsObj.find("div", {"class": "top-feature-overlay-cont"})

    # ITERATE OVER TAGS AND GRAB ARTICLE TITLES
    nameList = list()
    for article in bigTitle:
        heading_data = article.text
        nameList.append(heading_data)
        infoStorage.write(heading_data+'\n')
        print (nameList)

    URLList = []
    possible_links = bigLink.find_all('a')
    for url in possible_links:
        if url.has_attr('href'):
            URLList.append(url.attrs['href'])
    infoStorage.write("https://www.aljazeera.com"+URLList[1]+'\n')

    dateURL = urlopen("https://www.aljazeera.com"+URLList[1])
    dateObj = BeautifulSoup(dateURL, features="html.parser")
    bigArticleDate = dateObj.findAll("time", {"class": "timeagofunction"})

    dateList = list()
    for date in bigArticleDate:
        article_date = date.text
        dateList.append(article_date)
        infoStorage.write(article_date)


    # smalltitle = bsObj.findAll("h2", {"class": "top-sec-smalltitle"})
    #
    # for article in smalltitle:
    #     heading_data = article.text
    #     print(heading_data)
    #
    #     article_file.write(heading_data)
    #     article_file.write("\n")
    #
    # smallLink = bsObj.find("div", {"class": "topFeature-sblock-wr"})
    #
    # smallURL = []
    # i = 0
    # possible_links = smallLink.find_all('a')
    # for url in possible_links:
    #     if url.has_attr('href'):
    #         smallURL.append(url.attrs['href'])
    #         print(smallURL[1])
    #         i = i + 1


run()
