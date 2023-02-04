# P1. 네이버 영화 페이지에 들어가자 마자 보이는 박스오피스 1위 ~ 10위까지의 정보를 파이썬으로 불러와서 보기좋게 출력하세요

import requests
from bs4 import BeautifulSoup

URL = 'https://movie.naver.com/'
response = requests.get(URL)
html_code = response.text
result = BeautifulSoup(html_code, 'html.parser') # class 'bs4.BeautifulSoup'

# 주의 사항
# 나에게 필요한 정보가 시간에 따라서 자동으로 바뀌기 때문에(박스오피스, 현재상영작, 개봉예정작,..)
# 파이썬으로 불러온 컨텐츠가 나에게 필요한 컨텐츠인지 확인을 해줘야 함

# 박스오피스 버튼 클릭
items = result.find_all('li', class_='item')
# 개발자 툴에서 li.item을 입력해보자 (5개)

for item in items: # class 'bs4.element.Tag', 'bs4.element.ResultSet'
    itemClass = item.get('class') # ['item', 'on'] ['item']
    print(item)
    # 우리가 웹페이지에서 보고 있는 컨텐츠와 파이썬으로 불러온 컨텐츠가 다를 수 도 있다
    # 내가 원하는 프로그램을 만들기 위한 정답은 없다
    
    if 'on' in itemClass: # requests의 한계로 실행 안됨
        itemText = item.text
        if itemText == '박스오피스':
            movieList = item.find('1위~10위까지 감싸고 있는 태그')
            
'''
일반적으로 웹 서비스들은 봇(데이터를 수집하는 프로그램)이
해당 서비스의 정보를 무단으로 수집해서 부가적인 또 다른 서비스를 만들 수 있으므로
봇이 해당 서비스에 접근할 수 없게 아예 막아버리거나
봇이 접근했을 때는 사람이 보는 것과 다른 것을 보여주도록 구성함
requests는 봇이므로 이러한 한계가 존재함
'''