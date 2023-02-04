# CSV 형식으로 저장한 박스오피스 1 ~ 10위 정보를 불러와서 보기 좋게 출력하시오
import datetime
dt_now = datetime.datetime.now().date()

with open(f'C:/Users/JJH/Desktop/movies/{dt_now}.txt', 'r', encoding='UTF-8') as file:
    header = file.readline()
    print(header.replace(',','\t'), end='')

    while True:
        buffer = file.readline()
        print(buffer.replace(',', '\t'), end='')
        if buffer == '':
            break