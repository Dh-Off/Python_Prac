# 딕셔너리 이용하여 영화 정보 알려주는 시스템

print("영화 예매 시스템")

movie = {"범죄도시(KR)":19, "토이스토리(US)":12, "버즈라이트이어(US)":12, "알포인트(KR)":19}
print("1. 영화목록 확인\n2. 영화등급 확인\n3. 영화국적 확인\n4. 영화시스템 종료")

while True:
    a = int(input("목록 선택(1~4) : "))
    
    if a<=0 or a>= 5:
        print("목록 다시선택")
    
    if a == 1:
        b = list(movie.keys())
        print(b)
    elif a == 2:
        b = list(movie.items())
        print(b)
    elif a == 3:
        a = input("검색할 국적 입력 (KR),(US) : ")
        for i in movie.keys():
            if a in i:
                print(i)
    elif a == 4:
        break