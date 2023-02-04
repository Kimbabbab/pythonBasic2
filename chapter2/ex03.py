from selenium import webdriver

driver_path = 'C:\\Users\\JJH\\Desktop\\chromedriver.exe'

URL = 'https://movie.naver.com/'
driver = webdriver.Chrome(executable_path = driver_path)
driver.implicitly_wait(3)

driver.get(URL)

# 검색어 입력 영역의 xPath(상대경로) 또는 fullXPath(절대경로)를 사용해서 검색어 입력 영역을 선택하도록 만드세요
# x -> XML(이제 안씀) -> JSON

# 검색창에 기생충 입력
xPath = '//*[@id="ipt_tx_srch"]'
element = driver.find_element_by_xpath(xPath)
print(element) # WebElement 객체의 정보
element.click()
element.send_keys('기생충')

# 검색버튼 클릭
fullXPath = '/html/body/div/div[2]/div/div/fieldset/div/button'
element = driver.find_element_by_xpath(fullXPath)
element.click()

# 검색목록에서 기생충 클릭
copySelector = '#old_content > ul:nth-child(4) > li:nth-child(1) > dl > dt > a'
element = driver.find_element_by_css_selector(copySelector)
element.click()