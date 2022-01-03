Test_num=int(input())
check=[]
triangle_num=[]
for i in range(Test_num):
    a=int(input())
    check.append(a)
n=0
Tn=int((n*(n+1))/2)
while True:
    n+=1
    Tn = int((n * (n + 1)) / 2)
    if Tn>1000:
        break
    triangle_num.append(Tn)

def find_triangle(num):
    for i in triangle_num:
        for j in triangle_num:
            for k in triangle_num:
                if i+j+k==num:
                    return 1
    return 0

for i in check:
    a=find_triangle(i)
    print(a)
