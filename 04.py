#로또를 추첨하고 자신의 로또를 입력 한 후 맞춘 개수와 등수를 출력하는 프로그램

import random

lotto = []
mylottoList = []
same = 0

while True:
    lucky = random.randint(1,45)
    if lucky not in lotto:
        lotto.append(lucky)
    if len(lotto) == 6:
        break
    
lotto.sort()
lottoR = str(lotto)

while True:
    mynum = input("자신의 로또 번호 6개를 입력하세요. (띄어쓰기 필수) ==> ").split(" ")
    for a in mynum:
        mylottoList.append(int(a))
        mylottoList.sort()
        
    if (len(mylottoList) == 6):
        print("나의 로또 번호는 ",mylottoList," 번 입니다.")
        break
    else:
        print("6자리를 입력해주세요.")

print("로또 추첨 번호는 ",lottoR," 입니다.")

score = [0,6,5,4,3,2,1]
for n in mylottoList:
    if n in lotto:
        same += 1
       
if same == 0:
    print("아쉽네요")
else :
    print("{}개 맞음, {} 등 당첨!".format(same,score[same]))
        
