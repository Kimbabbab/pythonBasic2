import matplotlib.pyplot as plt

figure = plt.figure()
graph = figure.add_subplot(1, 1, 1)

data = [1, 2, 3]
label = ['Good', 'Bad', 'Normal']

graph.pie(data, labels=label, autopct='%d%%') # pie chart

plt.show()

'''
형식 지정자
    데이터를 출력할 때 어떤 형태로 출력할 지 지정하는 것
    정수로 출력할거다 : %d
    실수로 출력할거다 : %f
    문자로 출력할거다 : %c
    문자열로 출력할거다 : %s
'''

# 데이터 시각화 != 데이터 그래프화
# 폰트의 위치