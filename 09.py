#기분에 따른 노래 추천받는 프로그램

import random

happysong = ["아이유 - 에잇","오마이걸 - 살짝 설렜어","조정석 - 아로하","오반 - 오떻게 지내"]
sadsong = ["먼데이키즈 - 가을안부","로이킴 - 그때 헤어지면 돼","임한별 - 이별하러 가는 길","양다일 - 미안해",""]
relaxsong = ["김동률 - 동행","백예린 - 0310","김필 - 그때 그 아인","오왠 - 오늘"]
sleepsong = ["태연 - 그대라는 시","아이유 - 밤편지","아이유 - 정거장","머크툽 - 숲의목소리"]


while True:
    feel = input("오늘 추천받고싶은 노래는?  없으면: x [신나는, 슬픔, 휴식, 수면] ==> ")

    if feel == "x":
        print("종료합니다.")
        break
    
    if feel == "드라이브":
        rec = random.choice(happysong)
        print("\n추천 노래는 ",rec,"입니다! 안전운전 하세요!")
    elif feel == "슬픔":
        rec = random.choice(sadsong)
        print("\n추천 노래는 ",rec,"입니다! 좋은일이 있을거에요")
    elif feel == "휴식":
        rec = random.choice(relaxsong)
        print("\n추천 노래는 ",rec,"입니다!.")
    elif feel == "수면":
        rec = random.choice(sleepsong)
        print("\n추천 노래는 ",rec,"입니다. 잘자요~")
    else:
        print("\n목록 중에 작성해주세요.\n")
