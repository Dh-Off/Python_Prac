# [수학, 영어]순 성적 점수 불러오기

jumsu = {'서진':[80,71], '형진':[85,90], '윤진':[77,64]} #수학, 영어 순

while True:
    c = int(input("1. 수학성적  |  2. 영어성적  |  3. 평균 성적  |  4. 끝내기  // 입력 : "))
    
    if c == 1:
        for k,v in jumsu.items():
            print(k,v[0],"\n")
    elif c == 2:
        for k,v in jumsu.items():
            print(k,v[1],"\n")
    elif c == 3:
        for k,v in jumsu.items():
            print(k,(v[1]+v[0])/2,"\n")
    elif c == 4:
        print("\n종료")
        break