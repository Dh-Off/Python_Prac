# 음료 메뉴 주문하기.

total = 0
drink = {"아메리카노": 3000 , "카페라떼": 3500, "카페모카": 3500, "초코라떼": 4000, "녹차라떼": 4000, "레몬차": 4500, "생강차": 5000, "아인슈페너": 5000, "밀크쉐이크": 5000}
save = {}
while True:
    order = input("주문할 메뉴를 입력하세요. : ")
    
    if order in drink:
        count = int(input("몇잔 주문하시겠습니까? : "))
        save[order] = count
        D = drink.get(order) *  count
        total += D
        to = input("추가로 주문 하시겠습니까? : ")
        if to == "네":
            continue
        else:
            break
    break

print("주문한 음료는 ",save,"이고 총 금액은 ",total,"원 입니다.")
        