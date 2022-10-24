#랜덤 숫자를 유저가 유추하며 랜덤 숫자를 맞추는 게임

import random

Rnum = random.randint(1,100)
count = 1

while True:
    print("1 ~ 100까지의 랜덤 수 맞추기")
    user = int(input("랜덤 숫자는 ? ==> "))
    
    if count == 10:
        print("10번의 시도를 넘겼습니다.")
        break
    
    if (user >= 0) and (user <= 100):
        if user > Rnum:
            print("입력한 숫자가 더 큽니다.\n")
            count += 1
        elif user < Rnum:
            print("랜덤 숫자가 더 큽니다.\n")
            count += 1
        elif user == Rnum:
            print("\n랜덤 숫자를 맞췄습니다!!!!!")
            print("랜덤수 찾기 시도 횟수는 {}번 입니다.\n".format(count))
        else :
            pass
    else:
        print("1~100의 숫자중 입력하세요\n")

print("랜덤숫자는 ",Rnum,"이었습니다.")
