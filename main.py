from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

TitleStorage = open('articleTitles.txt', 'w')
URLStorage = open('articleURLS.txt', 'w')
DateStorage = open('articleDates.txt', 'w')

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
        TitleStorage.write(heading_data + '\n')
        #print (nameList)

    URLList = []
    possible_links = bigLink.find_all('a')
    for url in possible_links:
        if url.has_attr('href'):
            URLList.append("https://www.aljazeera.com"+url.attrs['href'])
    URLStorage.write(URLList[1] + "\n")


    #print(URLList[1])  # has link to big article

    #print("\n")

    smalltitle = bsObj.findAll("h2", {"class": "top-sec-smalltitle"})

    for article in smalltitle:
        heading_data = article.text
        #print(heading_data)

        TitleStorage.write(heading_data)
        TitleStorage.write("\n")

    smallLink = bsObj.find("div", {"class": "col-md-6 middle-east-bot"})

    smallURL = []
    i = 0
    possible_links = smallLink.find_all('a')
    for url in possible_links:
        if url.has_attr('href'):
            if i==0 or i==3 or i==6 or i==9:
                smallURL.append(url.attrs['href'])
                URLStorage.write("https://www.aljazeera.com"+ url.attrs['href'] + "\n")

            i = i + 1

            URLList.append(url.attrs['href'])

# dateURL = urlopen("https://www.aljazeera.com" + URLList[1])
# dateObj = BeautifulSoup(dateURL, features="html.parser")
# bigArticleDate = dateObj.findAll("time", {"class": "timeagofunction"})
#
# dateList = list()
# for date in bigArticleDate:
#     article_date = date.text
#     dateList.append(article_date)
#     DateStorage.write(article_date)

run()
