'''
데이터 시각화
 -> 데이터를 시각적으로 보여주는 것

 -> 대표적으로 그래프 방식으로 보여줌
  --> matplotlib 라이브러리 설치(pip)
 -> 워드 클라우드(유행지남)
 
 -> 웹 개발의 프론트엔드 개발자가 담당

'''

import matplotlib.pyplot as plt
from matplotlib import font_manager
import matplotlib

# 월별 카드 사용량(음식, 교육, 취미)
'''
<< 1월의 카드 사용량 >>
음식 - ***************
교육 - *****
취미 - ***************
'''

food = [15, 17, 13, 16, 14, 16, 13, 14, 15, 14, 16, 17]
edu = [5, 4, 15, 17, 15, 17, 15, 17, 25, 26, 24, 25]
hob = [15, 14, 6, 5, 4, 5, 5, 6, 4, 5, 4, 4]

for count in range(12):
    print(f'<< {count +1}월의 카드 사용량 >>')
    print(f'음식 - {"*" *food[count]}')
    print(f'교육 - {"*" *edu[count]}')
    print(f'취미 - {"*" *hob[count]}')

figure = plt.figure()
graph = figure.add_subplot(1, 1, 1)

x = [str(n)+'월' for n in range(1,13)]
# 내 PC에 설치된 폰트 > C:\Windows\Fonts
fontPath = 'C:/Windows/Fonts/ariblk.ttf'
fontSetting = font_manager.FontProperties(fname=fontPath).get_name()

matplotlib.rc('font', family=fontSetting)

graph.plot(x, food)
graph.plot(x, edu)
graph.plot(x, hob)

plt.show()