#4문제 이상의 문제 입력,
#4지선다형 출제 문제 답

#답이 맞으면 모든 문제를 푼 후 정답 갯수를 알려준다

import random

word=[['delivery date','납품일'],['on sale','할인 중인'],['cut price','할인 가격'],['rock-bottom price','최저 가격'],['quote','견적서'],
      ['resolve','해결하다'],['reimburse','변상하다'],['recall','회수하다'],['FOB(free on board)','본선 인도'],
      ['replacement','교체품'],['customer rights','소비자 권리'],['guarantee','품질보증'],
      ['price gap','가격 차이'],['cut by','가격을 ~만큼 깎다.'],['low-cost','저비용의'],
      ['bulk order','대량주문'],['customs clearance','통관'],['OA(Open Account)','외상거래']]                                         

n = int(input('문제 갯수: '))

mlist = random.sample(range(len(word)),n)

count=0


for i in mlist:
    smpl = random.sample(m,4)
    
    if i in smpl:
        k = smpl.index(i)                          

    else:

        k = random.randint(0,3) 

        smpl[k]=i
    print(word[i][0])


    for i in range(4):
        print('%d.'%(i+1)+word[smpl[i]][1],end='  ')
        
    print()
    dap=int(input('답: '))
    if dap-1 == k:
       print('정답입니다.')
       count += 1
    else:

        print('땡! 정답:',k+1)
    print()

print()
print('정답 수 : %d \n수고하셨습니다.'%count) 