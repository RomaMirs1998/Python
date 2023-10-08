import requests # allows us to download html from a website
from bs4 import BeautifulSoup # allows us to use html tags as objects in python
import pprint # allows us to print objects in a pretty way

res = requests.get("https://news.ycombinator.com/news") # downloads the html from the website
res2 = requests.get("https://news.ycombinator.com/news?p=2") # downloads the html from the website

#print(res.text) # prints the html of the website

#We use BeautifulSoup to clean up the html and make it easier to read and use
# Parse -> BeautifulSoup Object
soup=BeautifulSoup(res.text, "html.parser") # parses the html and creates a BeautifulSoup object
soup2=BeautifulSoup(res2.text, "html.parser") # parses the html and creates a BeautifulSoup object

#print(soup.body) # prints the body of the html
#print(soup.body.contents) # prints the contents of the body of the html
#print(soup.find_all("div")) # prints all the div tags in the html
#print(soup.find_all("a")) # prints all the a tags in the html
#print(soup.title) # prints the title of the html
#print(soup.a) # prints the first a tag in the html
#print(soup.find("a")) # prints the first a tag in the html
#print(soup.find(id="score_37785300")) # prints the first tag with the id score_37785300
#print(soup.select(".score")) # prints all the tags with the class score

links =soup.select(".titleline") # selects all the tags with the class titleline
subtext = soup.select(".subtext") # selects all the tags with the class subtext
links2 =soup2.select(".titleline") # selects all the tags with the class titleline
subtext2 = soup2.select(".subtext") # selects all the tags with the class subtext

mega_links = links + links2
mega_subtext = subtext + subtext2
def create_custom_hn(links, subtext):
    hn=[]
    for inx,item in enumerate(links):
        title = links[inx].getText() # gets the text of the tag
        aTag = links[inx].select("a") # gets the a tag of the tag
        href = aTag[0].get("href", None) # gets the href of the tag
        vote = subtext[inx].select(".score") # gets the score of the tag
        if len(vote):
            points = int(vote[0].getText().replace(" points",""))
            if points > 99:
                hn.append({"title": title, "link": href, "votes": points})
    return sort_stories_by_votes(hn)

def sort_stories_by_votes(hn):
    return sorted(hn, key=lambda k:k["votes"], reverse=True)



news = create_custom_hn(mega_links, mega_subtext)
pprint.pprint(news)