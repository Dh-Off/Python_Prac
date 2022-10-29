#컴퓨터가 정한 1~10 사이의 수를 5번의 기회 안에 정답을 맞추기

#컴퓨터가 정한 1~10 사이의 수를 5번 안에 정답 맞추기

import random
com = random.randint(1,10)

while True:
    for i in range(5):
        print(i+1,"회차 -",end='')
        user = int(input(" 랜덤 숫자는 ? (1 ~ 10) 입력 : " ))
        if user == com:
            print("\n◆정답입니다.◆\n")
            break
        elif user > com:
            print("\n랜덤 숫자보다 큽니다.\n")
        elif user < com:
            print("\n랜덤 숫자보다 작습니다.\n")
    
    a = input("다시하려면 z 입력 : ")
    if a == 'z':
        continue
    else:
        print("게임을 종료합니다.")
        break
