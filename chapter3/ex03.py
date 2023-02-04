import matplotlib.pyplot as plt

figure = plt.figure()
graph = figure.add_subplot(1, 1, 1)

'''
꺾은선 그래프에서 하나의 데이터를 보여주는 코드
x = [0, 1, 2, 3, 4] # x축 데이터
y = [4, 1, 3, 5, 2] # y축 데이터

graph.plot(x, y) # 꺾은선 그래프를 그리겠다
'''

# 꺾은선 그래프에서 두개의 데이터를 보여주는 코드
x1 = [0, 1, 2, 3, 4]
y1 = [4, 1, 3, 5, 2]

x2 = [0, 1, 2, 3, 4]
y2 = [0, 8, 5, 3, 1]

graph.plot(x1, y1)
graph.plot(x2, y2)

plt.show()