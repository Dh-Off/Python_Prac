#입력한 자연수의 약수와 소인수분해의 결과

def div(Num,v):
    while Num <= 0:
        print("\n1 이상의 자연수를 입력해주세요.\n")
        Num = int(input("자연수를 입력 :"))
    for i in range(Num+1):
        for k in range(Num+1):
            if i*k == Num:
                numList.append(i)
            k += 1
        i += 1

def Fac(Num,v):
    while Num != 1:
        if Num % v != 0:
            v += 1
        else:
            Num //= v
            NUM.append(v)   
    
numList,NUM = [], []
v = 2
Num = int(input("자연수를 입력하세요 : "))

div(Num,v)
Fac(Num,v)

print(Num,"의 약수는 {} 이고,\n소인수분해 결과는 {} 이다.".format(numList,NUM))
