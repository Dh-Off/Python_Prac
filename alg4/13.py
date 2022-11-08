#컴퓨터 2대가 가위바위보 게임을 10000번 진행 후 결과 출력

import random 
result = []

for i in range(10000):
    com1 = random.choice(["가위","바위","보"])
    com2 = random.choice(["가위","바위","보"])

    if com1 == "가위":
        if com2 == "바위":
            result.append("com2")
        elif com2 == "보":
            result.append("com1")

    elif com1 == "바위":
        if com2 == "가위":
            result.append("com1")
        elif com2 == "보":
            result.append("com2")

    elif com1 == "보":
        if com2 == "가위":
            result.append("com2")
        elif com2 == "바위":
            result.append("com1")

    if com1 == com2:
        result.append("비김")    

#print(result)
com1_count,com2_count,eq = 0, 0, 0

for j in range(len(result)):  #.count
    if result[j] == "com1":
        com1_count += 1
    elif result[j] == "com2":
        com2_count += 1
    elif result[j] == "비김":
        eq += 1
print("com1 승리 :",com1_count," || ","com2 승리 :",com2_count," || ","비긴판 :",eq)

if com1_count > com2_count:
    print("com1 승리")
elif com1_count == com2_count:
    print("판수 전부 같음. 무승부")
else:
    print("com2 승리")