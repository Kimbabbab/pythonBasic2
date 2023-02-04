''' <Problem 1>
import requests
from bs4 import BeautifulSoup

URL = 'https://movie.naver.com/movie/sdb/rank/rpeople.nhn'
params = {}
response = requests.get(URL, params=params)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
movie_in = soup.find_all('td', class_='title')

for number, movie in enumerate(movie_in):
    print(f'{number +1} : {movie.find("a").text.strip()}')
'''

''' <Problem 2>
import requests
from bs4 import BeautifulSoup

URL = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
params = {}
response = requests.get(URL, params=params)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
movieList = soup.find_all('div', class_='tit3')

for index, movie in enumerate(movieList):
    print(f'{index +1}위: {movie.find("a").text.strip()}')
'''

''' <Problem 3>
import requests
from bs4 import BeautifulSoup

URL = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
params = {}
response = requests.get(URL, params=params)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
movie_list = soup.find_all('tr')
up_list = []

for movie in movie_list:
    target_list = movie.find_all('td', class_='ac') # 0개 or 3개
    if target_list:
        target = target_list[1]
        if target.find('img', class_='arrow').get('alt') == 'up':
            up_list.append(movie.find('td', class_='title').text.strip())

for up_movie in up_list:
    print(up_movie)
'''