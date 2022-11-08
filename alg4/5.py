#심사위원 5명이 각 10점만점으로 점수를 주고 점수의 평균을 구하는 문제

score = []
i, sum = 0, 0
while i<5:
    n = int(input("점수 입력 : "))
    if n <= 0 or n >= 11:
        print("1~10점 입력")
        continue
    score.append(n)
    i += 1  

for k in score:
    sum += k

print("점수는",score,"점이고 평균은",sum/5,"입니다.")
