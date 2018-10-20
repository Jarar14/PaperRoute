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
    bigLink = bsObj.find("div", {"class": "top-feature-overlay-cont"})

    bigURL = []
    possible_links = bigLink.find_all('a')
    for url in possible_links:
	    if url.has_attr('href'):
		    bigURL.append(url.attrs['href'])
        
    print(bigURL[1]) #has link to big article

    # ITERATE OVER TAGS AND GRAB ARTICLE TITLES
    for article in bigtitle:
        heading_data = article.text
        print(heading_data)

        article_file.write(heading_data + " // ") #article title

        
        article_file.write('\n') #newline before next entry

    print("\n")

    smalltitle = bsObj.findAll("h2", {"class": "top-sec-smalltitle"})
    
    """


    smallLink = bsObj.find("div", {"class": "topFeature-sblock-wr"})

    smallURL = []
    possible_links = smallLink.find_all('a')
    i = 0
    for url in possible_links:
	    if url.has_attr('href'):
		    smallURL.append(url.attrs['href'])
		    print(smallURL[i])
		    i +=1
"""
		    
    for article in smalltitle:
        heading_data = article.text
        print(heading_data)

        article_file.write(heading_data)
        article_file.write("\n")

run()
