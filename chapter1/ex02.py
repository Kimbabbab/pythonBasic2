'''
백엔드 웹개발

requests
 -> 요청
response
 -> 응답

https://www.naver.com/
URL의 구성요소
프로토콜://서버의주소:포트번호
https://www.naver.com:80/

응답과 관련된 응답코드
 - 200번대 : 클라이언트의 요청에 문제가 없었고 요청한 서비스를 제대로 응답했다
 - 300번대 : 클라이언트의 요청에 문제가 없었으나 요청한 서비스가 다른 곳으로 이동했다
 - 400번대 : 클라이언트의 요청에 문제가 있어 요청한 서비스를 응답하지 못한다(URL 또는 파라미터를 잘못 사용)
            파라미터(Parameter) : 서비스가 요청을 처리하기 위해 필요한 부가적인 데이터
             e.g) 검색창에 입력한 데이터
 - 500번대 : 클라이언트의 요청에 문제가 있는지 없는지 모르겠지만
            서버에 문제가 생겨서 응답을 할 수 없다
            
웹 서비스를 요청했을 때 !항상! 응답코드(상태코드)를 먼저 확인해야 함

https://search.naver.com(기본경로)/search.naver(부가경로)
?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=코리아it아카데미
// ? 뒤에 있는 것은 get parameter 앞에는 URL

파라미터1&파라미터2&파라미터3&...&파라미터N
 └이름=값

'''

import requests

# requests.get("네이버 서비스의 URL")
# 해당 URL의 HTML 코드를 반환한다
response = requests.get('https://www.naver.com')

print(response) # 응답코드 출력
print(response.text)
# 텍스트가 너무 방대하다.. 읽기 좋게 Parsing(구문분석)이 필요하다