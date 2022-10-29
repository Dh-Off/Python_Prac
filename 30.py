#컴퓨터가 생각하는 숫자와 내가 생각하는 숫자 둘 중 누가 더 큰지?
#컴퓨터 = (1~100)
import random

com = random.randint(1,100)
user = int(input("생각중인 숫자 입력 ==> "))

if user == com:
    print("컴퓨터의 숫자와 같습니다.")
elif user > com :
    print("내가 생각한 숫자가 더 큽니다.")
elif user < com :
    print("컴퓨터가 생각한 숫자가 더 큽니다.")

print("컴퓨터 숫자는 : {}입니다.".format(com))