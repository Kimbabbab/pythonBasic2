'''
find(찾고자 하는 컨텐츠의 경로) : 찾고자 하는 컨텐츠 중 첫 번째 컨텐츠를 찾아주는 함수

find_all(찾고자 하는 컨텐츠의 경로) : 찾고자 하는 컨텐츠를 전부 찾아주는 함수

'''

import requests
from bs4 import BeautifulSoup

URL = "https://www.naver.com"
response = requests.get(URL)
htmlCode = response.text

result = BeautifulSoup(htmlCode, 'html.parser') # html 분석기를 사용해 htmlCode를 분석하라
contents_list = result.find_all('a') # 모든 <a> 태그를 찾아라
# print(type(contents_list)) # class 'bs4.element.ResultSet'

'''
반복문과 contents_list를 사용해서 찾은 모든 a태그를 화면에 출력하세요
1. contents_list에 들어있는 데이터 유형을 파악한다
왜? 그래야 그 유형에 맞춰서 활용할 수 있으니까
print(type(contents_list[0])) # class 'bs4.element.Tag'
print(type(contents_list[0].text)) # class 'str'
'''

'''
2. 데이터의 유형에 맞춰서 활용한다
firstContents = contents_list[0]
print(firstContents)
print(firstContents.text)
'''

# 우리가 find_all로 찾은 결과물에서 메일 메뉴 버튼이 몇 번째에 들어있는지 출력해보세요
# 메뉴 버튼의 HTML 코드엔 '메일'이라는 텍스트가 들어있다
for index, contents in enumerate(contents_list):
    if '메일' in contents.text:
        target = index
        print(index +1)
        print(contents)

# 네이버 메일 메뉴 버튼(Copy selector)
contents = result.find('#NM_FAVORITE > div.group_nav > ul.list_nav.type_fix > li:nth-child(1) > a')
# print(contents)

'''
bs4.element.Tag 타입 객체
 -> text 멤버 변수 : 그 태그가 가지고 있는 텍스트 컨텐츠를 반환
 -> get() 함수 : 그 태그가 가지고 있는 특정한 속성값을 반환
'''

classAttr = contents_list[target].get('class') # class Attribute(속성)
print(f'메뉴 버튼의 class 속성의 값 = {classAttr}') # ['nav'] : 클래스 속성은 여러개일 수 있다
hrefAttr = contents_list[target].get('href')
print(f'메뉴 버튼의 hrefAttr 속성의 값 = {hrefAttr}')