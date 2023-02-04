''' <Problem 1>
class File:
    def save(self, path):
        print(f'{path}에 파일을 저장합니다')
    def read(self, path):
        print(f'{path}에 저장된 파일을 읽어옵니다')

class Xlsx(File):
    def function(self, type):
        print(f'{type} 함수를 실행합니다')

class PPT(File):
    def presentation(self, page):
        print(f'{page}페이지부터 발표를 실행합니다')

file = File()
file.save('바탕화면')
file.read('바탕화면')
print('='*5)

xlsxFile = Xlsx()
xlsxFile.read('바탕화면')
xlsxFile.function('sum')
xlsxFile.save('내문서')
print('='*5)

PPTFile = PPT()
PPTFile.read('바탕화면')
PPTFile.presentation(0)
PPTFile.save('내문서')
'''

''' <Problem 2>
class Piano:
    def __init__(self):
        self.keyList = list('도레미파솔라시')
        self.sound = ''

    def pressPedal(self):
        print('~'*5)

    def pressKey(self, key):
        if key not in self.keyList:
            print('누를 수 없는 건반입니다')
            return False
        print(key + self.sound)

class GrandPiano(Piano):
    def __init__(self): # 생성자 오버라이딩
        super().__init__() # 인스턴스 멤버 변수는 자동으로 상속되지 않는다
        self.sound = '~' # 상속 받은 멤버 변수 변경

class UplightPiano(Piano):
    def __init__(self):
        # super().__init__()
        self.keyList = list('도레미파솔라시')
        self.sound = '!'

grandPiano = GrandPiano()
uplightPiano = UplightPiano()

grandPiano.pressKey('또')
grandPiano.pressKey('도')
grandPiano.pressPedal()

uplightPiano.pressKey('쏠')
uplightPiano.pressKey('솔')
uplightPiano.pressPedal()
'''