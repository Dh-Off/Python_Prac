#배스킨라빈스 31 게임


from random import randint

goal = 0
com_num, my_num = 0,0

print("=====│             '베스킨라빈스 31 게임'               │=====")
print("=====│ 순차적으로 번호를 말하고 31을 말하는 사람이 패배 │=====")
print("=====│       말할 수 있는 숫자의 최대 갯수는 3 개       │=====\n")
    
while True :
    if goal < 31 :
        com_num = randint(1,3)          #컴퓨터가 말할 숫자 1~3개 중 랜덤으로 결정
        goal += com_num                 #컴퓨터가 말한 숫자를 goal에 더한 후 저장
        print("\n컴퓨터는",com_num,"을(를) 말했습니다. ","  현재 숫자 =",goal)

        if goal >= 31 :                 #컴퓨터가 말한 숫자가 31 이상일때 컴퓨터의 패배
            print("컴퓨터 '패배'  // 사용자 '승리'  \n")
            continue
        else :
            my_num = int(input("말할 숫자의 개수 입력 : "))
            
            while (my_num <= 0) or (my_num > 3) :                   #사용자가 입력한 숫자의 개수가 0 혹은 음수이거나, 3 을 초과한 숫자를 입력시
                my_num = int(input("※※ 1 ~ 3 중 입력하세요 : "))   # 1 ~ 3 중에 선택할때 까지 입력
                
            goal += my_num       #사용자가 입력한 숫자를 goal에 더한 후 저장
            print("\n\n현재 숫자 =",goal,"\n")
            if goal >= 31 :
                print("컴퓨터 '승리' // 사용자 '패배'  \n")     #사용자가 입력한 숫자가 31 이상이 될때, 컴퓨터가 게임에서 승리
                
    else:
        print("31 이상입니다.  게임을 종료합니다.")
        break