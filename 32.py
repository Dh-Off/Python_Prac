# 속이 빈 삼각형, 역삼각형  피라미드

"""
a = ""
for i in range(1,10):
    for k in range(0,i):
        a += "*"
    a += "\n"
print(a)

b = ""
for w in range(1,10):
    for e in  range(10,w,-1):
        b += "*"
    b += "\n"
print(b)
"""

a = int(input("수 입력 : "))
b, c, b1, c1 = "","","",""
for i in range(1,a+1):
    for j in range(a,i,-1):
        b += ' '
    for j in range(0,2*i-1):
        b += "*"
    b += "\n"
print(b)


for i in range(1,a-1):
    for j in range(a-1,i-1,-1):
        b1 += ' '
    for j in range(0,2*i-1):
        b1 += "*"
    b1 += "\n"
print(b1)

################################

for l in range(a-2,0,-1):
    for k in range(l,a):
        c1 += ' '
    for k in range(1,2*l):
        c1 += "*"
    c1 += "\n"
print(c1)


for l in range(a,0,-1):
    for k in range(l,a):
        c += ' '
    for k in range(1,2*l):
        c += "*"
    c += "\n"
print(c)




