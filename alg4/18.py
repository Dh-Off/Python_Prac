#여러 숫자중 홀수만 추출해서 사용자 선택에 따라 내림/오름차순으로 정렬

import random
num,i = [],0

for _ in range(10):
    n = random.randint(1,50)
    num.append(n)
print("전체 숫자는 ",num)

while i <len(num):
    if num[i]%2 != 0:
        i += 1
        continue
    else:
        num[i]%2 == 0
        del(num[i])
print("홀수는 ",num)

while True:
    a = int(input("1. 내림차순  |  2. 오름차순 : "))
    if a == 1:
        print(sorted(num))
    elif a == 2:
        print(sorted(num, reverse=True))
    else:
        print("다시입력")
        continue