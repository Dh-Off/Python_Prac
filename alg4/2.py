#5개 서로 다른 자연수 입력받고, 최댓값 찾고 몇번째 수 인지

number = []
i,f = 0, 0
while i <5:
    a = int(input("자연수 입력 : "))
    while True:
        if a in number:
            print("같은수가 있음. 다시입력")
        elif a <= 0:
            print("자연수 입력")
        else:
            number.append(a)
            i +=1
            break
        break
for f in range(5):
    if max(number) == number[f]:
        break
    
print("\n리스트 : ",number)
print("최댓값은",max(number),"\n순서는 0, 1, 2, 3, 4 번 순이며 ",f,"번째에 최댓값이 있습니다.")
