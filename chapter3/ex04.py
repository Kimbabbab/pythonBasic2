import matplotlib.pyplot as plt

figure = plt.figure()
graph = figure.add_subplot(1, 1, 1)

x = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
y = [8, 6, 5, 4, 7, 9, 5]

graph.bar(x,y) # bar chart

plt.title('weekday call')
plt.xlabel('week')
plt.ylabel('call')
plt.show()