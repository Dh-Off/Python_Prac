#표준 체중을 구하고 비만측정 프로그램
#표준 체중을 기준으로 감량 및 중량을 출력

"""
성별에 따른 공식 = 
    남자 : 키(m): * 키(m) * 22
    여자 : 키(m): * 키(m) * 21
"""

def weight():
    while True:
        G = int(input("남자 : [1]  여자 : [2] 입력 ==> "))
        if (G > 2)or(G <= 0):
            print("\n[1], [2] 중 다시입력\n")
            continue
        else:
            height = float(input("현재 키 입력 : "))/100
            weight = float(input("현재 몸무게 입력 : "))
            
            if G == 1:
                avg_weight = height * height * 22
                print("\n키 {}cm 남자의 표준 체중은 {:.2f}kg입니다.".format(height*100,avg_weight))
            elif G == 2:
                avg_weight = height * height * 21
                print("\n키 {}cm 여자의 표준 체중은 {:.2f}kg입니다.".format(height*100,avg_weight))   

            Over = weight - avg_weight
            Low = avg_weight - weight

            if weight > avg_weight:
                print("평균보다 {:.2f}kg 감량을 권장합니다.\n".format(Over))
            else :
                print("평균보다 {:.2f}kg 증량을 권장합니다.\n".format(Low))
    
weight()
