'''
To run this code on ur machine, u need to install the following using pip

Beautiful soup --> pip install beautifulsoup4
Requests --> pip install requests
html5lib --> pip install html5lib
'''


import requests
from bs4 import BeautifulSoup

'''
Inputs: The url u need to scrape, the class of articles in html of the website, the tag of article.
Example: For the website 'https://thehackernews.com/', class of articles is 'story-link' and tag is 'a'.
Click on InspectElement and u will be able to see these easily. Going Forward , we will figure out how
to get all the articles by using the "next" link in the page.

The Output will be the links of all the articles in the first page. Since it is only POC, we've scraped
the articles in the first page only.

'''
def getArticlesFromUrl(url, classOfArticleInHTML, HTMLtag):
    #Getting the content of web page
    request = requests.get(url)
    firstPage = request.content

    #Creating soup for beautifulSoup(Simply creating an object of BeautifulSoup)
    #html5lib is the parser. It is the latest one.
    soup = BeautifulSoup(firstPage, 'html5lib')

    #Get all the articles in the website
   
    articles = soup.find_all(HTMLtag, class_ = classOfArticleInHTML)

    #Get the links of the articles collected
    articleLinks = []
    for article in articles:
        articleLinks.append(article['href'])
    
    return articleLinks



'''
Inputs: the list of links and all other inputs are self explanatory

The Function gathers the text in the given link(We will provide the links of the articles we gathered before)
and creates a file with the same title as article and fills it with article's content.

It's important to know that it's a little complicated to define a general function for all the websites. However,
We tried to define a general function. 

This is a little custom built for the first website 'https://thehackernews.com/'. 

Little tweaks in the code will do the trick for all the websites cause they are not entirely different. 
'''
def getContentFromLinks(linksList, HTMLtagOfTitle, classOfTitle, HTMLtagOfBody, classOfBody):
    for link in linksList:
        request = requests.get(link)
        content = request.content

        soup = BeautifulSoup(content, 'html5lib')

        title = soup.find(HTMLtagOfTitle, class_= classOfTitle).get_text()

        body = soup.find_all(HTMLtagOfBody, class_=classOfBody)

        text = body[0].get_text().split()

        finalContent = ''

        i = 0
        while i < len(text):
            if text[i] == '(function':
                while text[i][-4:] != "nt);":
                    i+=1
            
            elif i%17 == 0:
                finalContent+= (text[i] + '\n')
                i+=1
            else:
                finalContent+= (text[i] + ' ')
                i+=1
        
        f = open(''+title +'.txt', 'w')
        f.write(title)
        f.write('\n')
        f.write(finalContent)



#Driver Code

links = getArticlesFromUrl('https://thehackernews.com/', 'story-link', 'a' )

getContentFromLinks(links,'h1','story-title','div','articlebody clear cf')