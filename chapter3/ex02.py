'''
figure -> 시트
subplot -> 그래프
시트 안에 그래프를 만든다
액셀(시트) 안에 차트를 만든다
'''

import matplotlib.pyplot as plt

figure = plt.figure() # 시트 생성
chart1 = figure.add_subplot(1, 2, 1) # 시트에 그래프를 그림(1행 2열)
chart2 = figure.add_subplot(1, 2, 2) # 시트에 그래프를 그림(1행 2열)

# chart3 = figure.add_subplot(1, 1, 1)
# (행번호, 열번호, 차트번호)
# add_subplot 함수는 차트를 핸들링 할 수 있는 객체를 리턴(chart1에 저장)

plt.show()