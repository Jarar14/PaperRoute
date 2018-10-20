from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv

article_file = open('day1.txt', 'w')

#linkData = open('linkDataFile.txt', 'r+') #for reading select url data


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
        print(heading_data)

        article_file.write(heading_data + " // ")  # article title

        article_file.write('\n')  # newline before next entry

    bigURL = []
    possible_links = bigLink.find_all('a')
    for url in possible_links:
        if url.has_attr('href'):
            bigURL.append(url.attrs['href'])

    print(bigURL[1])  # has link to big article

    print("\n")

    smalltitle = bsObj.findAll("h2", {"class": "top-sec-smalltitle"})

    for article in smalltitle:
        heading_data = article.text
        print(heading_data)

        article_file.write(heading_data)
        article_file.write("\n")

    smallLink = bsObj.find("div", {"class": "col-md-6 middle-east-bot"})

    print("\n---Small Link data---\n")

    smallURL = []
    i = 0
    possible_links = smallLink.find_all('a')
    for url in possible_links:
        if url.has_attr('href'):
            #smallURL.append(url.attrs['href'])
            if i==0 or i==3 or i==6 or i==9:
                #print(url.attrs['href'], "\n")
                smallURL.append(url.attrs['href'])
                #linkData.write(url.attrs['href'] + i + "\n")
            
            i = i + 1

    for i in smallURL:
        print(smallURL[i])
run()
