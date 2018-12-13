"""

THIS CODE ON RUNNING WILL PULL LATEST NEWS FROM "TIMES OF INDIA" AND WILL LIST THEM ALONG WITH SHORT DESCRIPTION

"""

import requests,json
from bs4 import BeautifulSoup

website='https://timesofindia.indiatimes.com/news'
response=requests.get(website)
page=response.content
news_html=BeautifulSoup(page,'html.parser')
news=news_html.find('div',attrs={'id':"ulItemContainer"})
news_list=news.findAll('li')
j=1
for i in news_list:
    try:
        title=i.a['title']
        href=i.a['href']
        link="https://timesofindia.indiatimes.com"+href
        response=requests.get(link)
        subpage_html=response.content
        news_subpage=BeautifulSoup(subpage_html,'html.parser')
    except Exception:
        continue
    try:
        print('\n',j,' -> ',end=' ')
        print(title,'\n')
        temp=news_subpage.find('script',attrs={'type':'application/ld+json'})
    except Exception:
        continue
    try:
        jsontemp=json.loads(temp.text)
        for q in jsontemp['speakable']['cssSelector']:
            print(q,end=' ')
        print()
    except Exception:
        print("No Description")
    j=j+1
    if(j>=11):
        break
