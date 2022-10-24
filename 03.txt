#점수를 입력하면 학점이 나오는 프로그램

def grade():

    if score >= 90:
        print("A", end='')
    elif score >= 80:
        print("B", end='')
    elif score >= 70:
        print("C", end='')
    elif score >= 60:
        print("D", end='')
    else :
        print("F", end='')

    print("학점입니다.")


while True:
    score = int(input("학점 입력하세요 ==> "))
    if (score > 100) or (score < 0):
        print("학점은 0점 ~ 100점 입니다.  // 다시입력해주세요")
    else :
        grade()
