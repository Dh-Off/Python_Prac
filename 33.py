#장르별 영화를 추천 프로그램

import random 

movie_mel = ["뷰티 인사이드","어바웃 타임","미 비포 유","비긴 어게인"]
movie_comi = ["화이트 칙스","수상한 그녀","극한직업","브루스 올마이티"]
movie_sad = ["7번방의 선물","안녕,헤이즐","인생은 아름다워","지금 만나러갑니다"]

Movie = [movie_mel,movie_comi,movie_sad]

while True:
    movie = input("추천 받고싶은 영화 장르 입력 : [멜로, 코믹, 슬픔]")
    if movie == '멜로':
        rec = random.choice(Movie[0])
        print("\n추천 영화는 ",rec," 입니다.\n")
    elif movie == '코믹':
        rec = random.choice(Movie[1])
        print("\n추천 영화는 ",rec," 입니다.\n")
    elif movie == '슬픔':
        rec = random.choice(Movie[2])
        print("\n추천 영화는 ",rec," 입니다.\n")
    else:
        print("\n[멜로, 코믹, 슬픔] 장르 중 골라주세요.\n")
