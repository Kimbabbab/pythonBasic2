class AddressInfo:
    # Python은 오버로딩이 없다
    def __init__(self, name, address, tel, memo):
        self.name = name
        self.address = address
        self.tel = tel
        self.memo = memo

    # 아래에 작성된 생성자가 우선됨
    def __init__(self, name=None, address=None, tel=None, memo=None):
        self.name = self.input_info('이름') if name == None else name
        # 인자값을 주면 멤버 변수에 그대로 저장하고
        # 인자값을 주지 않으면(default: None) 인스턴스 메서드를 활용해
        # 사용자로부터 멤버 변수에 저장할 값을 입력 받는다
        self.address = self.input_info('주소') if address == None else address
        self.tel = self.input_info('연락처') if tel == None else tel
        self.memo = self.input_info('메모') if memo == None else memo

    def input_info(self, info_type):
        while True:
            info = input(f'{info_type} >> ').strip()
            if info == '': continue
            if info_type != '연락처': break
            if info_type == '연락처': # 형식 : aaa-bbbb-cccc
                infoToken = info.split('-')
                # 연락처에 -(하이픈)이 들어있고 3묶음인지 판단
                check1 = len(infoToken) == 3
                # check1 = info.count('-') == 2
                if not check1:
                    print('연락처를 형식(aaa-bbbb-cccc)에 맞게 입력해주세요')
                    continue
                # 연락처의 각 자리 숫자가 3, 4, 4자 인지 판단
                check2 = len(infoToken[0]) == 3 and len(infoToken[1]) == 4 and len(infoToken[2]) == 4
                if not check2:
                    print('연락처를 형식(aaa-bbbb-cccc)에 맞게 입력해주세요')
                    continue
                break
        return info

    def print_info(self):
        print(self.info_to_str())

    def info_to_str(self):
        str = ''
        str += f'이름 => {self.name}\n'
        str += f'주소 => {self.address}\n'
        str += f'연락처 => {self.tel}\n'
        str += f'메모 => {self.memo}'
        return str