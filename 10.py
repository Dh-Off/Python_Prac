#정해진 문 중에 컴퓨터가 고른 문을 찾기



import random


door = ['A','B','C','D','E']
com_door = random.choice(door)

while True:
    find = input("[A, B, C, D, E] 문 중에 열려있는 문을 고르세요.")

    if find not in door:
        print("\n잘못 찾았습니다. 다시 찾아주세요.\n")
    else:
        if find == com_door:
            print("\n★★열려있는 문입니다.★★\n")
        else :
            print("\n닫혀있는 문입니다!!\n")

