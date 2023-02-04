'''
<< 셀레니움(Selenium)을 사용해서 크롤링, 스크래핑 하는 방법 >>
1. Selenium 라이브러리 설치 : cmd 창에서 pip install selenium
(PIP Installs Packages)
2. 크롬 브라우저의 버전 확인
3. 크롬 브라우저의 버전에 맞는 Web Driver 다운
4. 파이썬 코드로 Selenium 라이브러리와 Web Driver를 사용해서
    필요한 데이터를 가져오도록 코드 작성
5. 가져온 데이터를 꺼내서 활용

프로그램 테스트 프레임워크
웹 애플리케이션(홈페이지) 테스트 프레임워크
frame work
 e.g) 스프링(웹), 유니티/언리얼(게임), 안드로이드(앱),...
https://chromedriver.chromium.org/downloads
크롬 드라이버 경로 : C:/Users/JJH/Desktop
'''

import selenium
print(selenium.__version__)