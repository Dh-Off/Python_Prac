import random

def Lotto():
    lottoList = []
    while True:
        lotto = random.randint(1,45)
        if lotto not in lottoList:
            lottoList.append(lotto)
        if len(lottoList) == 6:
            break
    print("로또 번호는 = ",lottoList," 입니다")

print("추첨 시작")
Lotto()

Num = int(input("로또번호 6새 입력 (띄어쓰기 구분) ==> ").split())

print(Num)
