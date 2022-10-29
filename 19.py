# 주사위 게임

#[ 컴퓨터 | 플레이어 ] 서로 100점 가지고 시작

#주사위눈에 따라 실점. 모두 잃는 쪽이 패배.

# 엔터를 입력할 떄 마다 게임 진행

import random

def dice():
    global user, com   
    user_dice = random.randint(1,6)
    com_dice = random.randint(1,6)
    
    print("\t 주사위 결과\n나 : {}\t\t\t컴퓨터 : {}".format(user_dice,com_dice))
    user -= user_dice
    com -= com_dice
    
print("엔터를 누르면 주사위가 굴려집니다. ")
user, com = 100,100

while True:
    enter = input("")
    while enter == "":
        dice()
        print("내 점수 = {0}점   ,컴퓨터 점수 = {1}점\n".format(user,com))
        print("계속 진행 ==> enter")
        break
    if (user <= 0) and (com >= 1):
        print("●컴퓨터 승리, ○나의 패배")
        break
    elif (com <= 0) and (user >= 1):
        print("●나의 승리, ○컴퓨터 패배")
        break

        
