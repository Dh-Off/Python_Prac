# 학점 구하는 프로그램
# 공식 = ((학점 수 x 교과목 평점) 합) / 수강신청 총 학점 수 = 평균학점

def grade(_):
    sub = int(input("◆과목 수 ==> "))
    score = {'A+':4.5,'A':4.0,'B+':3.5,'B':3.0,'C+':2.5,'C':2.0,'F':0}
    C1,CG,CG1 = 0,0,0
    print("---- 학점 별 성적 : ",score)
    for i in range(sub):
        C,G = map(float,input("학점과 평점을 입력 (띄어쓰기 구분) ==> ").split())
        C1 += C      #학점 
        CG += C*G    #학점*평점 = CG
    CG1 = CG/C1      #학점 / 평점
    print("◆◆",sem,"학기에 들은 학점 : ",C1)
    print("◆◆ 평점은 : {:.1f}\n".format(CG1))

while True:
    num = int(input("학기 수를 입력하세요 [1, 2] ==> "))
    if num <= 0 or num >= 3:
        num = int(input("학기 수를 입력하세요 [1, 2] ==> "))
    else:
        break
for sem in range(num):
    sem += 1
    grade(sem)
