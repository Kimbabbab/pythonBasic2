''' <Problem 1>
def score_to_grade(score):
    if 100 >= score >= 90: # 100 >= score and score >= 90
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'

print(score_to_grade(95))
print(score_to_grade(30))
print(score_to_grade(130))
'''

''' <Problem 2>
def year_to_age(year):
    age = 2022 - year
    return age
print(year_to_age(1999))
'''

''' <Problem 3>
def max(a, b, c):
    max = a
    if b > max: max = b
    if c > max: max = c
    return max
print(max(2,3,1))
print(max(1,2,3))
'''

''' <Problem 4>
def coffee_machine(money):
    coffee = money // 300
    change = money % 300
    print(f'자판기에서 뽑을 수 있는 커피는 {coffee}잔이고 잔돈은 {change}원입니다')
coffee_machine(1000)
coffee_machine(650)
'''

''' <Problem 5>
def make_fruitList(size):
    basket = []
    for i in range(size): # 0~size-1
        basket.append(input('리스트에 저장할 과일 이름 >> '))
    return basket
print(make_fruitList(4))
'''

''' <Problem 6>
def inputScores(kor, eng, mat):
    scoreList = []
    scoreList.append(kor)
    scoreList.append(eng)
    scoreList.append(mat)
    return scoreList

def calcScore(scoreList):
    sum = 0
    for score in scoreList:
        sum += score
    avg = sum / len(scoreList)
    print('성적의 총점은 %d점, 평균은 %.2f점입니다' %(sum, avg))

calcScore(inputScores(90,60,85))
'''

''' <Problem 7>
def middleChar(str):
    return str[len(str) //2]
print(middleChar('apple'))
print(middleChar('banana'))
'''

''' <Problem 9>
def second_to_watch(sec):
    hour = sec // 3600
    sec = sec % 3600
    min = sec // 60
    sec = sec % 60
    watch = {}
    watch['hour'] = hour
    watch['minute'] = min
    watch['second'] = sec
    return watch
print(second_to_watch(3710))
'''

''' <Problem 10>
def sum(num1, num2):
    sum = 0
    low = min(num1, num2)
    high = max(num1, num2)
    for num in range(low, high+1):
        sum += num
    print(f'{num1}과 {num2}사이의 합계는 {sum}입니다')
sum(1, 10)
sum(10, 1)
'''

''' <Problem 11>
def swap(val1, val2): // local variable(함수를 위한 공간에 선언)
    temp = val1
    val1 = val2
    val2 = temp
    // 지역 변수 소멸
val1 = 10 // global variable
val2 = 20
swap(val1, val2)
print(val1, val2) // 전역 변수에 영향을 미치지 않는다
'''

''' <Problem 12>
def calc():
    operand1 = int(input('숫자 입력 -> '))
    operand2 = int(input('숫자 입력 -> '))
    operator = input('연산자 입력 -> ')
    expr = f'{operand1} {operator} {operand2}'
    print(f'{expr} = {eval(expr)}')
calc()
'''