# 두 수에 대한 사칙연산 계산기                  두 수에 대한 계산기이므로 2개 숫자 이상의 연산 x
# +, -, *, /    이외 연산자는 재입력             

def calcul():
    while True:
        num1 = (input("[숫자1] [기호] [숫자2] 순으로 입력 : "))
        result = num1.split(" ")
        
        if result[1] == "+":
            a = int(result[0])+int(result[2])
        elif result[1] == "-":
            a = int(result[0])-int(result[2])
        elif result[1] == "*":
            a = int(result[0])*int(result[2])
        elif result[1] == "/":
            a = int(result[0])/int(result[2])
        elif result[1] == int(result[1]):
            print("사칙연산 기호중 입력하세요.\n")
        else:
            print("사칙연산 기호중 입력하세요.\n")
            continue
        print(int(result[0]),result[1],int(result[2])," = ",end='')
        print("결과는 {:.2f}\n".format(a))
        
        
print("사칙연산 기호 [ +, -, *, / ] 사용  ◆띄어쓰기 구분 필수◆\n")
calcul()
        
        
