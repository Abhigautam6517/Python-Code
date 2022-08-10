import bs4
import urllib.request as url

# findMovie = input("Enter your Movie Name")
# url = 'https://www.imdb.com/chart/top/';

response = url.urlopen('https://www.imdb.com/chart/top/');

page = bs4.BeautifulSoup(response)

moviesName = page.find_all('td',class_="titleColumn")
# print(moviesName.text)

# for i in range(10):
#     if(findMovie==moviesName[i].text):

#         print(moviesName[i].text())
#         print("Movie is find")
#         break
# else:
#     print("Movie not found")

# movies = []
# for movie in range(len(moviesName)):
#     # movie = movie.get_text().replace("\n","")
#     # movie = movie.strip(" ")
#     movies.append(movie)
# print(movies[movie].text)