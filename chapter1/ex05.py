import requests
from bs4 import BeautifulSoup

URL = "https://www.naver.com"
response = requests.get(URL)
print(response) # 상태코드 꼭 확인해주자!
htmlCode = response.text

result = BeautifulSoup(htmlCode, 'html.parser')
contents = result.find('a', id_='NM_FAVORITE', class_='nav')
print(contents)
contentsList = result.find_all('a', class_='nav')
print(contentsList)