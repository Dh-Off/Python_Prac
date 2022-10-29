#로또 추첨을 위한 1~45 사이 난수 생성 및 6자리 수 생성후 출력 프로그램

import random

def Lotto():
    lottoList = []
    while True:
        lotto = random.randint(1,45)
        if lotto not in lottoList:
            lottoList.append(lotto)
        if len(lottoList) == 6:
            break
    print("오늘 로또 번호는 = ",lottoList," 입니다")

print("추첨 시작")
Lotto()
