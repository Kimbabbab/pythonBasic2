''' <Problem 1>
class BookInfo:
    def __init__(self, name, author):
        self.name = name
        self.author = author

    def printInfo(self):
        print(f'제목 = {self.name}')
        print(f'저자 = {self.author}')

book1 = BookInfo('취업을 위한 코딩 테스트', '나동빈')
book2 = BookInfo('알고리즘 인터뷰', '박상길')
book3 = BookInfo('파이썬 자료구조', '시바타 보요')

book1.printInfo()
book2.printInfo()
book3.printInfo()
'''

''' <Problem 2>
class Person:
    def __init__(self, name):
        self.name = name
        print(f'{name} is born')

man = Person('james')
woman = Person('emily')
'''

''' <Problem 3>
class Watch:
    def __init__(self):
        str = input('시간을 입력하세요 (HH:mm:ss) -> ')
        self.hour = int(str[:2])
        self.minute = int(str[3:5])
        self.second = int(str[-2:])

    def addHour(self, hour): # 시간 업데이트
        self.hour = (self.hour + hour) % 24

    def addMinute(self, minute): # 시간, 분 업데이트
        hour = (self.minute + minute) // 60
        self.addHour(hour)
        self.minute = (self.minute + minute) % 60 # 0~59

    def addSecond(self, second): # 시간, 분, 초 업데이트
        minute = (self.second + second) // 60
        self.addMinute(minute)
        self.second = (self.second + second) % 60

    def printInfo(self):
        print(f'계산된 시간은 {self.hour}시 {self.minute}분 {self.second}초입니다')

watch = Watch()
watch.addHour(int(input('더 할 시간을 입력하세요 -> ')))
watch.addMinute(int(input('더 할 분을 입력하세요 -> ')))
watch.addSecond(int(input('더 할 초를 입력하세요 -> ')))
watch.printInfo()
'''

''' <Problem 4>
import math

class Cylinder:
    def getVolumn(self):
        return math.pi * (self.radius ** 2) * self.height
    def getArea(self):
        topArea = math.pi * (self.radius ** 2)
        sideArea = 2 * math.pi * self.radius * self.height
        return 2 * topArea + sideArea
    
cylinder = Cylinder()
cylinder.radius = 4 # radius 멤버 변수 생성
cylinder.height = 5 # height 멤버 변수 생성

print(f'원기둥의 부피 : {cylinder.getVolumn()}')
print(f'원기둥의 겉넓이 : {cylinder.getArea()}')
'''

''' <Problem 5>
class Song:
    def __init__(self, name, genre):
        self.name = name
        self.genre = genre

    def printInfo(self):
        print(f'대표곡 : {self.name}({self.genre})')

class Singer: # 멤버 변수 : name(str), song(Song)
    def __init__(self, name):
        self.name = name

    def hitSong(self, song):
        self.song = song

    def printInfo(self):
        print(f'가수이름 : {self.name}')
        self.song.printInfo()

song = Song('이별택시','발라드')
singer = Singer('김연우')
singer.hitSong(song)
singer.printInfo()
'''

''' <Problem 6>
class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def printInfo(self):
        print(f'name = {self.name} / price = {self.price}')

food1 = Food('치킨', 18000)
food2 = Food('피자', 28000)
food3 = Food('초밥세트', 22000)

food1.printInfo()
food2.printInfo()
food3.printInfo()
'''

''' <Problem 7>
class Menu:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def printMenuInfo(self):
        print(f'{self.name}({self.price}원)')

class Bill:
    def __init__(self, orderNumber, menuList):
        self.orderNumber = orderNumber
        self.menuList = menuList

    def printTotalPrice(self):
        print(f'주문 번호 : {self.orderNumber}')
        print('주문한 메뉴')
        total = 0
        for menu in self.menuList:
            menu.printMenuInfo()
            total += menu.price
        print('='*10)
        print(f'결제 금액 : {total}')

menu1 = Menu('짜장',4900)
menu2 = Menu('짬뽕',5900)
menu3 = Menu('탕수육',13900)

menuList = [menu1, menu2, menu3]

bill = Bill(1, menuList)
bill.printTotalPrice()
'''

''' <Problem 8>
import random

class Account:
    def __init__(self, number, balance):
        self.number = number
        self.balance = balance

    def transfer(self, target, money):
        if self.balance < money:
            return False
        else:
            target.getMoney(money)
            self.balance -= money
            return True

    def getMoney(self, money):
        self.balance += money

    def printInfo(self):
        print('='*20)
        print(f'account number = {self.number}')
        print(f'account balance = {self.balance}')
        print('=' * 20)

accountNumberList = set()
while True:
    accountNumber = random.randint(10000, 99999)
    accountNumberList.add(accountNumber)

    if len(accountNumberList)==2:
        break
accountNumberList = list(accountNumberList)

accountA = Account(accountNumberList[0], random.randint(100000,500000))
accountB = Account(accountNumberList[1], random.randint(100000,500000))

while True:
    result = accountA.transfer(accountB, 2770)
    if not result:
        break

accountA.printInfo()
accountB.printInfo()
'''