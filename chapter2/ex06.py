'''
구글 플레이 스토어(https://play.google.com/store/) 에서
게임 카테고리의 인기 앱/게임 정보를 수집해 파일에 저장하세요
 - 앱 이름
 - 썸네일 이미지 경로 ( img )
 - New 여부 ( span.sT93pb.w2kbF.K4Wkre )
 - 카테고리 ( span.sT93pb.w2kbF / 선택자로 태그를 불러온 뒤 두번째 태그를 사용해야 함 : New 여부와 겹침 )
 - 평균 별점 ( div.ubGTjb div )
 - ?
'''

from selenium import webdriver

class AppInfo:
    def __init__(self, appName, appImg, appCategory, appStarScore, appDetailPage):
        self.appName = appName
        self.appImg = appImg
        self.appCategory = appCategory
        self.appStarScore = appStarScore
        self.appDetailPage = appDetailPage

driver_path = 'C:/Users/JJH/Desktop/chromedriver.exe'
URL = 'https://play.google.com/store/'
driver = webdriver.Chrome(executable_path=driver_path)
driver.implicitly_wait(3)
driver.get(URL)

divList = driver.find_elements_by_css_selector('#yDmH0d > c-wiz.SSPGKf.glB9Ve > div > div > div.N4FjMb.Z97G4e > '
                                               'c-wiz > div > c-wiz > c-wiz:nth-child(2) > c-wiz > section > div > '
                                               'div:nth-child(3) > div > div > div > div.aoJE7e.b0ZfVe > div')
                                              # ... > div:nth-child(1~15)
count = 1
appInfoList = []
for div in divList:
    appInfoWrappers = div.find_elements_by_css_selector('div.VfPpkd-WsjYwc')
    for appInfoWrapper in appInfoWrappers:
        appNameTag = appInfoWrapper.find_element_by_css_selector('span.sT93pb.DdYX5.OnEJge')
        appNameData = appNameTag.text

        appImgTag = appInfoWrapper.find_element_by_tag_name('img')
        appImgData = appImgTag.get_attribute('src')

        # appIsNewTag = appInfoWrapper.find_element_by_css_selector('span.sT93pb.w2kbF.K4Wkre')
        # appIsNewData = appIsNewTag.text

        appCategoryTag = appInfoWrapper.find_elements_by_css_selector('span.sT93pb.w2kbF')[1]
        appCategoryData = appCategoryTag.text

        appStarScoreTag = appInfoWrapper.find_element_by_css_selector('div.ubGTjb div')
        appStarScoreData = appStarScoreTag.get_attribute('aria-label')

        appDetailPageTag = appInfoWrapper.find_element_by_tag_name('a')
        appDetailPage = appDetailPageTag.get_attribute('href')

        print(count, appNameData)
        count += 1
        print(appImgData)
        # print(appIsNewData) # 예외 처리 필요
        print(appCategoryData)
        print(appStarScoreData)
        print(appDetailPage)
        print('-'*5, '-'*5)

        appInfo = AppInfo(appNameData, appImgData, appCategoryData, appStarScoreData, appDetailPage)
        appInfoList.append(appInfo)

'''
a 태그
 -> 컨텐츠를 클릭할 수 있게 해주는 태그
 -> 컨텐츠를 클릭하면 다른 페이지로 이동할 수 있음
    a 태그의 href 속성을 활용하면 됨
'''

'''
- 앱의 기본정보를 수집하는 프로그램

- 위에서 수집한 기본 정보를 열어서
    그 안에 있는 appDetailPage 값을 활용해서
    각 앱의 상세 정보를 수집하는 프로그램
'''