title = input("나눌 문장 입력 : ")

split_s = input("기준이 될 문자열을 입력하세요.")
ss = len(split_s)

if split_s in title:
    while True:
        for i in range(len(title)):
            if title[i] == split_s:
                print("['{}','{}']".format(title[:i],title[i+1:]))
            else:
                i += 1
        break
else:
    print("문장안에 나눌 문자열이 없습니다.")
    
                



"""
if split_s in title:
    print(title[:ss])
else:
    print("문장안에 나눌 문자열이 없습니다.")


안녕하세요


하 = split_s[2]

:split_s
안녕  세요
"""
