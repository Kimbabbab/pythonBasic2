'''
주소록 관리 프로젝트 (중요!!)
 -> 구성요소 : CRUD (모든 프로그램의 전부)
 C Create : 추가 / 저장 (ex. 회원가입, 상품 등록, 캐릭터 생성)
 R Read : 검색         (ex. 로그인, 상품 검색, 캐릭터 정보창)
 U Update : 수정       (ex. 회원 정보 수정, 상품 정보 수정)
 D Delete : 삭제       (ex. 회원 탈퇴, 상품 정보 삭제)

proc(process=program)
 -> 일의 과정이나 공정
 -> 프로그램
Thread
 -> 실행 중인 프로그램
프로젝트(=프로그램)
 -> 완성된 기능을 가지고 있는 프로그램

- 화면 구성 예시 -
주소록 추가(C)
주소록 검색(R)
주소록 수정(U)
주소록 삭제(D)

파이썬에서 사용자와 상호작용 할 수 있는 기능
 -> input()

예외 처리
 -> 파이썬 : 오류(Error, Exception)
 -> 자바 : Exception

상수 : 변하지 않는 고유한 값
 e.g) 3.14, '안녕하세요'
상수에 이름을 붙이는 방법
 -> C언어 : #define
    ex) #define ADD 1
 -> C++ : const
    ex) const int ADD = 1;
 -> Java : final
    ex) final int ADD = 1;
 -> 파이썬은 상수에 이름을 붙이는 방법이 없음
    그래서 변수를 활용해서 상수에 이름을 붙였다 라고 생각
    ADD = 1
    
주소록 정보
 -> 이름 : 홍길동 / 고영희
 -> 주소 : 서울 / 경기도
 -> 연락처 : 010-1111-1111 / 010-2222-2222
 -> 메모 : 옆집 친구 / X

지금 우리가 저장하려고 하는 것
 -> 데이터 X
 -> 정보 O
프로그램 개발 시 [정보]를 다뤄야한다면 클래스를 사용해야함!
'''

import constant.menu_name_constant as menu_name
from frame.addressInfo import AddressInfo # AddressInfo class

# 정보(이름/주소/연락처/메모)를 입력받고
# 입력받은 정보를 검증하는 함수
def input_info(info_type):
    # info_type == '연락처'일 때 형식 확인 누락
    while True:
        info = input(f'{info_type} >> ').strip()
        if info != '': break
    return info

addressInfoList = []

# 주소록 정보 불러오기
with open('addressBook.csv', 'r', encoding='UTF-8') as file:
    infoList = file.readlines()
    for info in infoList:
        info = info[4:-1].split(',') # 개행문자 제거
        addressInfo = AddressInfo(info[0], info[1], info[2], info[3])
        addressInfoList.append(addressInfo)

while True:
    print('<< 주소록 관리 프로그램 >>')
    print('1. 주소록 추가')
    print('2. 주소록 검색')
    print('3. 주소록 수정')
    print('4. 주소록 삭제')
    print('5. 프로그램 종료')

    menu = int(input('어떤 기능을 실행하시겠습니까?(번호로 입력해주세요) >> '))

    if menu == menu_name.ADDRESS_ADD_MENU:
        print('<< 주소록 추가 화면 >>')
        # 사용자에게 추가할 주소록 정보를 입력 받는다
        '''
        name = input_info('이름')
        address = input_info('주소')
        tel = input_info('연락처')
        memo = input_info('메모')
        '''

        '''
        print(f'이름 => {name}')
        print(f'주소 => {address}')
        print(f'연락처 => {tel}')
        print(f'메모 => {memo}')
        # 사용자가 입력할 때 "사용자는 내가(개발자) 기대한 값을 입력할거다" 라고 절대로 생각하면 안됨!!
        # 이름을 입력하지 않고 enter치면? 예외처리하자!
        '''

        # 사용자가 입력한 주소록 데이터를 클래스를 활용해서 하나의 주소록 정보로 합침
        # addressInfo = AddressInfo(name, address, tel, memo)
        # addressInfo = AddressInfo(input_info('이름'), input_info('주소'), input_info('연락처'), input_info('메모'))
        addressInfo = AddressInfo()

        # 사용자가 입력한 주소록 정보를 저장한다
        # 변수? 리스트? 딕셔너리? 리스트!
        addressInfoList.append(addressInfo)
        print('!! 주소록을 추가했습니다 !!')

    elif menu == menu_name.ADDRESS_SELECT_MENU:
        print('<< 주소록 검색 화면 >>')

        # 1. 검색할 연락처를 입력 받는다
        #  - 입력을 받을 때는 예외 처리를 한다! (!= 오류)
        # 2. 저장된 연락처와 비교한다
        # 3. 저장된 n번째 연락처와 입력 받은 연락처가 일치한다면
        # 해당 주소록의 정보를 출력한다

        findAddressInfo = AddressInfo('', '', '', '') # None이 아니다
        # 사용자로부터 입력을 받지 않는다
        findAddressInfo.tel = findAddressInfo.input_info('연락처')
        # targetTel = input('검색할 연락처를 입력하세요 >> ') 유효성 검사 누락
        exist = False
        for nthAddressInfo in addressInfoList:
            if findAddressInfo.tel == nthAddressInfo.tel:
                nthAddressInfo.print_info()
                exist = True
        if not exist:
            print('저장되지 않은 연락처입니다')
            print('연락처를 확인하고 다시 입력하세요')

    elif menu == menu_name.ADDRESS_UPDATE_MENU:
        print('<< 주소록 수정 화면 >>')
        
        # 1. 수정할 주소록을 검색하기 위해 연락처를 입력 받는다
        # 2. 저장된 연락처와 비교한다
        # 3. 저장된 연락처와 일치하는 연락처가 있다면
        #       (수정을 위한 코드) : 주소와 메모만 수정
        # 4. 저장된 연락처와 일치하는 연락처가 없다면 안내문구 출력

        findAddressInfo = AddressInfo('', '', '', '')  # None이 아니다
        findAddressInfo.tel = findAddressInfo.input_info('연락처')
        # targetTel = input('검색할 연락처를 입력하세요 >> ') 유효성 검사 누락
        exist = False
        for nthAddressInfo in addressInfoList:
            if findAddressInfo.tel == nthAddressInfo.tel:
                nthAddressInfo.address = nthAddressInfo.input_info('수정할 주소')
                nthAddressInfo.memo = nthAddressInfo.input_info('수정할 메모')
                print('!! 주소록이 수정되었습니다 !!')
                exist = True
        if not exist:
            print('저장되지 않은 연락처입니다')
            print('연락처를 확인하고 다시 입력하세요')

    elif menu == menu_name.ADDRESS_DELETE_MENU:
        print('<< 주소록 삭제 화면 >>')

        findAddressInfo = AddressInfo('', '', '', '')  # None이 아니다
        findAddressInfo.tel = findAddressInfo.input_info('연락처')
        # targetTel = input('검색할 연락처를 입력하세요 >> ') 유효성 검사 누락
        exist = False
        for index, nthAddressInfo in enumerate(addressInfoList):
            if findAddressInfo.tel == nthAddressInfo.tel:
                addressInfoList.pop(index)
                print('!! 주소록을 삭제했습니다 !!')
                exist = True
        if not exist:
            print('저장되지 않은 연락처입니다')
            print('연락처를 확인하고 다시 입력하세요')

    elif menu == menu_name.PROGRAM_EXIT_MENU:
        # 주소록 정보 저장
        with open('addressBook.csv', 'w', encoding='UTF-8') as file:
            for index, nthAddressInfo in enumerate(addressInfoList):
                csvData = f'{index +1} > {nthAddressInfo.name},{nthAddressInfo.address},' \
                          f'{nthAddressInfo.tel},{nthAddressInfo.memo}\n'
                file.write(csvData)

        print('프로그램을 종료합니다')
        break
    else:
        print('올바른 메뉴 번호를 입력하세요')