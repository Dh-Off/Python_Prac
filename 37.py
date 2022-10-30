# 컴퓨터가 1~100사이 랜덤숫자 뽑고 유저가 10회안에 맞추기  (성공실패 유무)

import random

com = random.randint(1,100)
count = 0
print("10번의 기회 안에 예상 숫자를 맞춰주세요. 범위 (1~100)")
while count < 10:
    count += 1
    print(count,"회 | ",end='')
    user = int(input("예상 수 입력 : "))
    if user>100 or user<=0:
        print("숫자는 1~100 사이 숫자입니다.")
    elif user == com:
        print("정답입니다!")
        break
    elif user > com:
        print("더 작은 수를 입력해주세요.\n")
    elif user < com:
        print("더 큰 수를 입력해주세요.\n")
if count == 10:
    print("{}회 초과로 실패했습니다. 랜덤숫자 = {}".format(count,com))
else:
    print("\n총 시도 횟수는 {}회 이고, 성공했습니다.".format(count))
