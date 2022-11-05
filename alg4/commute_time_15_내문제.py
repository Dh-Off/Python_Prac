import datetime

def time(name):
    global Date, record
    now = datetime.datetime.now()       #현재시간 사용
    HMS = "\n%Y년 %m월 %d일 "
    YDT = "%H시 %M분 %S초"
    Date = now.strftime(HMS)
    record = now.strftime(YDT)          #년월일과 시분초 나눠서 표기
    print(Date,"| ",end='')             #날짜 표기
   
company = {}
       
print("※ 출퇴근 기록 명부입니다. ※  ▶ 명부 확인 = c 입력 ◀")
while True :
    name = input("\n\n이름을 입력해주세요.  : ") 
    time(name)                              #함수실행
    if name in company:
        comlist = list(company.get(name))
        com = ''.join(map(str,comlist))         #company의 키에 대한 값을 리스트로 만든 후에 문자열로 변환
        print("{} | {} ＊퇴근\n\n {}".format(name,record, com))
        del company[name]               
        continue                          #퇴근시간이 기록되면 해당 사람의 키,값 모두 제거 후 반복문이동
    
    company[name] = "출근 ▷ " + record        #출근시간 정보 기록
    
    if name == 'c':
        del company['c']             #'c' 입력받을 시 목록에 들어간 'c' 제거 후 키 목록으로 이동
        break      
    print("{} | {} ＊출근\n\n {}".format(name,record,company))      #출근시간 기록
   

morning = list(company.keys())       #현재 출근한 사람들의 명단  / 퇴근하면 명단에서 제외
print("현재 출근 명단",morning)
