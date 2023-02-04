'''
네이버 영화 메인 페이지에 있는
박스오피스 1~10위 데이터를 가져오는 프로그램
'''

from selenium import webdriver
import movieModule
import datetime
dt_now = datetime.datetime.now().date()

driver_path = 'C:\\Users\\JJH\\Desktop\\chromedriver.exe'
URL = 'https://movie.naver.com/'
driver = webdriver.Chrome(executable_path = driver_path)
driver.implicitly_wait(3)
driver.get(URL)

# 박스오피스 메뉴를 클릭
element = driver.find_element_by_css_selector('#BOXOFFICE_tab > a')
# <a> 태그 : 클릭할 수 있는 태그(anchor)
element.click()

# 박스오피스 1~10위 컨텐츠(태그)를 가져오기
moviesWrapper = driver.find_element_by_css_selector('#flick0')
movies = moviesWrapper.find_elements_by_tag_name('li')

movieList = []
rank = 1

for movie in movies:
    # 데이터1(시청 등급) 추출
    spans = movie.find_elements_by_css_selector('div.obj_off a span')
    for span in spans:
        classAttr = span.get_attribute('class') # class 'str'

        if classAttr.find('ico_rating') != -1:
            data1 = span.text
            print(f'시청 등급 => {data1}')

        '''
        if classAttr == 'rank':
            data4 = span.text
        '''

    # 데이터2(포스터 이미지의 경로) 추출
    img = movie.find_element_by_css_selector('div.obj_off a img')
    data2 = img.get_attribute('src')
    print(f'포스터 이미지의 경로 => {data2}')

    # 데이터3(영화 제목) 추출
    data3 = img.get_attribute('alt')
    # data3 = movie.find_element_by_css_selector('p.mv_title').text
    print(f'영화 제목 => {data3}')

    # 데이터4(영화 순위) 추출
    data4 = rank
    print(f'영화 순위 => {data4}')
    rank += 1

    # 데이터5(주말 관객수) 추출
    span = movie.find_element_by_css_selector('div.obj_off a span.baseplate')
    spans = span.find_elements_by_css_selector('strong span')

    data5 = ''
    for nth in spans:
        data5 += nth.text
    data5 = data5[:-1].replace(',', '') # '명', ',' 제거
    print(f'주말 관객수 => {data5}')

    nthMovie = movieModule.Movie(data1, data2, data3, data4, data5)
    movieList.append(nthMovie)

'''
<span> 태그 : 텍스트를 출력하는 태그
영화 정보
    -> 데이터1 : 시청 등급 ( div.obj_off a span )
    -> 데이터2 : 포스터의 인터넷 경로 ( div.obj_off a img )
    -> 데이터3 : 영화 제목
    -> 데이터4 : 영화 순위
    -> 데이터5 : 주말 관객수 ( div.obj_off a span.baseplate )
    -> 데이터6 : ?
'''

'''
파이썬 -> 객체지향프로그래밍에 영향을 받은 언어
OOP -> 클래스, 객체, 상속 등
프로그램을 개발할 때 정보를 저장할 때는 무조건 객체를 사용해서 정보를 저장해야함!
'''

# 위 for문을 돌면서 추출한 박스오피스 1~10위까지 영화 정보를 파일에 저장

with open(f'C:/Users/JJH/Desktop/movies/{dt_now}.txt', 'w', encoding='UTF-8') as file:
    file.write('시청 등급,포스터의 인터넷 경로,영화 제목,영화 순위,주말 관객수\n')
    for movie in movieList:
        # f string -> 최근에(3.~) 추가된 문자열을 생성하는 방법 중 하나
        csv = f'{movie.ratingsOfViewers},{movie.posterImageUrl},' \
              f'{movie.movieTitle},{movie.movieRank},{movie.weekendAttendance}'
        file.write(csv + '\n')