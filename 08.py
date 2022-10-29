#사용자가 고른 숫자를 컴퓨터가 맞추는 업다운 프로그램

import random
print("컴퓨터가 내 숫자 맞추기\n")

cum = []
count = 1
for _ in range(0,100):
    cum.append(count)
    count += 1

P = int(input("1~100 중 내 숫자 입력 ==> "))

while P not in range(1,101):
    P = int(input("1~100 사이의 값을 입력 "))

while True:
    Num = cum[(len(cum)//2) -1 ]
    print("컴퓨터 숫자 ",Num)

    if P == Num:
        print("컴퓨터가 숫자 맞추기 성공")
        break
    
    e = input("사용자가 up / down 중 입력")

    if (P < Num) and (e == "down"):
        cum = cum[:cum.index(Num)]
 
    elif (P > Num) and (e=="up"):
        cum = cum[cum.index(Num) +1:]
        
    else:
        print("범위 벗어남")



"""
===================================================== (수정하기)
#랜덤으로 출력 후 업다운 맞추기

import random
print("컴퓨터가 내 숫자 맞추기\n")
Num = random.randint(1,100)


P = int(input("1~100 중 내 숫자 입력 ==> "))

while P not in range(1,101):
    P = int(input("1~100 사이의 값을 입력 "))

print("컴퓨터 숫자 ",Num)

while True:

    if Num == P:
        print("컴퓨터가 숫자 맞추기 성공")
        break
    
    e = input("사용자가 up / down 중 입력")

    if (Num >= P) and (e == "down"):
        Num = (Num-P)//2+1
        print("\n컴퓨터 : ",Num)
        
    elif (Num <= P) and (e=="up"):
        Num = (Num+P)//2+1
        print("\n컴퓨터 : ",Num)
        
    else:
        print("범위 벗어남")
"""