#컴퓨터 2대가 가위바위보 게임을 10000번 시켜서 결과를 리스트 저장, 최종적으로 누가 더 많이 이겼는지 결과 확인

import random 
result = []

for i in range(100):
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

print(result)
com1_count,com2_count = 0, 0

for j in range(len(result)):
    if result[j] == "com1":
        com1_count += 1
    elif result[j] == "com2":
        com2_count += 1
print(com1_count," == ",com2_count)

if com1_count > com2_count:
    print("com1 승리")
elif com1_count == com2_count:
    print("판수 전부 같음. 무승부")
else:
    print("com2 승리")