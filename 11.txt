#입력한 값에 대한 진약수를 구하고 진약수의 합을 구하는 프로그램
#진약수 = 자기 자신을 제외한 양의 약수

numList = []
Num = int(input("진약수를 구할 숫자 입력 : "))
Listsum = 0

while Num <= 0:
    print("\n1 이상의 숫자를 입력해주세요.\n")
    Num = int(input("진약수를 구할 숫자 입력 : "))

while True:
    maxmin = Num // Num  #처음 약수
    numList.append(maxmin)
    for i in range(Num):
        for k in range(Num):
            if i*k == Num:
                numList.append(i)
                k += 1
                i += 1               
    print(Num,"의 약수는 ",numList,"입니다.")
    for hap in numList:                         #리스트총합
        Listsum += hap
    break
print("입력한 진약수의 총 합은 ",Listsum," 입니다.")  


    

    
