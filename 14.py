#젤라또, 와플 가게 추가 결제 프로그램

import random

sum_gel,sum_waf = 0,0

def pay(sum_gel,sum_waf):
    return (sum_gel + sum_waf)
    
def store(qq):
    while True:
        global sum_gel, sum_waf    
        if qq == 1:
            gelnum= int(input("젤라또 수량 입력 : "))  
            sum_gel += (gelnum * 500)      #젤라또 금액 합계
            break
        
        elif qq == 2:
            wafnum = int(input("와플 수량 입력 : "))
            sum_waf += (wafnum * 2000)     #와플 금액 합계
            break
        
        elif qq == 3:
            Sum = pay(sum_gel,sum_waf)     #젤라또, 와플 금액 총계
            print("\n◆총 금액은",Sum,"입니다. ")
            if Sum <= 0:
                print("추가 후 선택해주세요.")        
            else:
                Y_pay = int(input("지불할 금액을 입력하세요 : "))
                if Sum > Y_pay:
                    print("잔액 부족, 다시 주문해주세요.")    #지불금액 비교
                    
                else:
                    Cur = Y_pay - Sum
                    print("\n계산 후 거스름 돈은 {}원 입니다.".format(Cur))
                    sum_gel, sum_waf = 0,0          
                    t = range(1,101)              #번호표 1~100번중 랜덤 출력 
                    print(random.choice(list(t)),"번 손님입니다. 감사합니다.\n")
                break
            break
        
while True:
    qq = int(input("1. 젤라또 500원  |  2. 와플 2000원  |  3. 결제 ==> "))
    store(qq)
