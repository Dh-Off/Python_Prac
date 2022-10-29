#편의점 재고 관리하기

store = {}
print("물품, 재고량 ◆◆입력◆◆")

while True:
    item = input("넣을 물품을 입력하세요. ==> ")
    if item == 'c':
          break 
    count = input("수량을 입력하세요. ==> ")
    store[item] = count

    print("\n입력 그만 = 'c'")

print("\n물품, 재고량 ◆◆검색◆◆")

while True:
    item = input("찾을 물품 입력 ==> ")
    if item in store:
        print("\n이 물품은 {}개 남았어요.".format(store[item]))
    elif item =='c':
        print("종료합니다.")
        break
    else:
        print("그 물품은 없어요.")
    print("\n입력 그만 =""c"" ")
