import bs4 
import urllib.request as url

response = url.urlopen('https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off')

page = bs4.BeautifulSoup(response)
# print(page);

# title = page.find('div',class_='_4rR01T')
# print(title.text);

titles = page.find_all('div',class_='_4rR01T')
for i in range(len(titles)):
    print(titles[i].text)
# print(title.text);