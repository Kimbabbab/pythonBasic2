# P2. 구글 플레이 앱으로 들어가서 여러분이 원하는 아무 앱에 작성된 리뷰를 파이썬으로 불러와 보기 좋게 출력하세요

import requests
from bs4 import BeautifulSoup

URL = 'https://play.google.com/store/apps/details?id=com.devsisters.ck&hl=ko&gl=US'
params = {
    'id' : 'com.devsisters.ck',
    'hl' : 'ko',
    'gl' : 'US'
}
response = requests.get(URL, params)
html_code = response.text
soup = BeautifulSoup(html_code, 'html.parser')

appNameTag = soup.find_all('div', class_='qxNhq') # 1개
# print(len(appNameTag)) # 1
appNameTag = appNameTag[0].find('span')
appName = appNameTag.text

print(f'이번에 리뷰를 가져올 앱은 {appName} 앱입니다')

reviews = soup.find_all('div', class_='Jwxk6d') # 1개 : 조상 태그
# print(len(reviews)) # 1
reviews = reviews[0].find_all('div', class_='EGFGHd') # 3개 : 부모 태그
# print(len(reviews)) # 3

for review in reviews:
    reviewTextTag = review.find('div', class_='h3YV2d') # 자식 태그
    reviewText = reviewTextTag.text
    print(reviewText)

''' (한번에 접근)
items = soup.find_all('div', class_='h3YV2d')
# 개발자 도구에 div.h3YV2d를 검색해보자 (3개)
for index, item in enumerate(items):
    print('{}번째 리뷰 >> {}'.format(index+1, item.text))
'''