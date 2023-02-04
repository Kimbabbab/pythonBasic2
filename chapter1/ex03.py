import requests

URL = 'https://search.naver.com/search.naver'
# response = requests.get(URL)
# param(parameter)
# 딕셔너리: 키와 값
param = {
    'query' : '파이썬'
}
# print(response)
# print(response.text)

# response = requests.get(url=URL, params=param)
# get 메서드는 파라미터가 아주 많다, 어떤 파라미터에 인자값을 넣어줄지 명시적으로 보여주자

# 200번 코드로 응답이 왔다고 해서 내가 원하는 결과가 전달된건 아님
# https://search.naver.com/search.naver?query=파이썬 웹으로 접속해보자
# print(response)
# print(response.text)

# https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=파이썬

params = {
    'where' : 'nexearch',
    'sm' : 'top_hty',
    'fbm' : '1',
    'ie' : 'utf8',
    'query' : '파이썬'
}
# response = requests.get(url=URL, params=params)

# print(response)
# print(response.text)

'''
요청 하는 방법
 1. requests 라이브러리 import
 2. requests.get(URL, PARAMETER)
 3. get 함수가 반환해주는 결과값을 변수(response)에 저장
 4. 변수를 그대로 출력해서 응답코드를 확인
 5. text 멤버 변수를 출력해서 결과값을 확인 또는 활용
'''

# 네이버 영화 서비스에서 기생충 영화 정보를 파이썬으로 불러오세요
URL = 'https://movie.naver.com/movie/bi/mi/basic.naver?code=161967'
params = {
    'code' : '161967'
}
response = requests.get(url=URL, params=params)
print(response)
print(response.text)
'''한계 : 컴퓨터가 요청을 하는 것이기 때문에 반복문을 사용해서
쉽게 불필요한 요청을 굉장히 많이 하도록 조작할 수 있음(DDoS) / 그래서 서버 자체에서
requests로 한 요청은 응답하지 않도록 설정한 서버도 있음
또한 필요한 데이터가 상대적이라거나 특정 시점의 데이터라면 요청을 못 할 수도 있음
이런 모든 한계가 없는게 서버 측에서 제공하는 API이다. 만약 제공해준다면 API를 쓰자'''