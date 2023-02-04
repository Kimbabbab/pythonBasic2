from selenium import webdriver
import time
# 클릭해서 install package selenium(파이참 연동)
# 구버전 : 3.141.0(파일 -> 설정 -> 프로젝트 -> Python 인터프리터)

driver_path = 'C:\\Users\\JJH\\Desktop\\chromedriver.exe'
URL = 'https://www.naver.com/'

driver = webdriver.Chrome(executable_path = driver_path)
driver.implicitly_wait(3) # 3~5초가 적당
# selenium이 web driver를 사용해서 chrome 브라우저를 실행시킨다
# 크롬 브라우저를 제어할 수 있는 객체를 리턴(driver에 저장)

driver.get(URL) # URL로 이동
# time.sleep(3) # 로드 타임

'''
1. 네이버 웹 페이지에 접속
2. 네이버 웹 페이지에 있는 검색어 입력 영역에 검색어를 입력하도록 명령
    검색어 입력 영역의 Selector : #query
    
find_element_~~~ : 선택자에 맞는 태그 하나를 찾아줌
find_elements_~~~ : 선택자에 맞는 태그들을 찾아줌

태그명 / 클래스명 / 아이디를 사용해서 태그를 찾을 수 있음
find_element_by_tag_name('태그명')
find_elements_by_tag_name('태그명')
find_element_by_class_name('클래스 속성의 값')
find_elements_by_class_name('클래스 속성의 값')
find_element_by_id('아이디')
find_elements_by_id('아이디') ? 프론트엔드 개발자의 실수로 동일 id가 여러개 존재할 수도 있다
'''

# Selector : #query
element = driver.find_element_by_id('query')
print(element)
# element 변수에 들어있는 태그를 선택
# element 변수에 검색어 입력 영역이 들어있으므로
# 검색어 입력 영역을 선택하는 것
element.click() # 검색창을 클릭

element.send_keys('네')
element.send_keys('이')
element.send_keys('버')

# 위에까지 해서 검색어 입력이 끝났음
# 이제는 해당 검색어로 검색 결과가 보여지도록
# 검색 버튼을 클릭해라 라는 명령을 내려보세요

# Selector : #search_btn
element = driver.find_element_by_id('search_btn')
element.click()

'''
웹 페이지에서 사용자가 무언가를 입력할 수 있는 태그 : input의 type 속성이 text임
웹 페이지에서 사용자가 선택지를 체크 선택할 수 있는 태그 : input의 type 속성이 checkbox임
웹 페이지에서 사용자가 선택지를 활성/비활성 선택할 수 있는 태그 : input의 type 속성이 radio임

<input type="text">
<input type="checkbox">
<input type="radio">
'''

'''
웹 페이지 로드(load) : 웹 페이지에 접속했을 때 내가 요청한 서비스를 보여주기까지 기다리는 시간(로드 타임)

웹 페이지는 로드 타임이 있으니까
지정한 페이지로 이동한 뒤 로드가 완료 될 때까지 기다려야 함
기다리는 방법
1. time.sleep(sec) : 무조건 지정한 초만큼 프로그램을 멈춤
2. driver변수(웹 페이지를 제어할 수 있는 객체를 가지고 있는 변수)의 메서드
    implicitly_wait(sec) : 웹 페이지가 로드될 때까지 최대 지정한 초만큼 프로그램을 멈춤
                            지정한 초전에 로드가 완료되면 멈추는걸 끝내고 그 다음 코드가 동작
                            지정한 초를 넘어서 계속 로드가 되고 있으면 예외를 발생시킴
                            만약 예외가 발생했다면 예외 처리를 하거나 sec의 값을 더 많이 늘려준다
'''

# 네이버 메인 우측 트렌드쇼핑 컨텐츠를 가져오자
#<li> 태그 : #goodsItem_5803239 // 쇼핑항목 하나의 id? 부모 태그를 이용하자
#<ul> 태그 : #contents_productAd > div.list_goods_wrap > ul

'''
time.sleep(5 + 3) # 트렌드쇼핑 컨텐츠가 웹 페이지 보다 늦게 로드된다(iframe)
trendShoppingWrapperTag = driver.find_element_by_css_selector('#contents_productAd > div.list_goods_wrap > ul')
print(trendShoppingWrapperTag)
elements = trendShoppingWrapperTag.find_elements_by_tag_name('li')
for element in elements:
    print(element)
'''

'''
iframe 태그를 사용해서 흩어진 컨텐츠를 보여주는 방법
    웹 페이지 안에서 iframe을 사용해 컨텐츠를 보여주면
    Selenium이 해당 컨텐츠를 불러올 수가 없음
'''