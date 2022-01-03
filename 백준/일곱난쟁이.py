leng=[]
for i in range(9):
    a=int(input())
    leng.append(a)
leng.sort()
trigger=0
check=[]
for i in range(len(leng)):
    for j in range(i+1,len(leng)):
        check=leng[:i]+leng[i+1:j]+leng[j+1:]
        if sum(check)==100:
            trigger=1
            break
    if trigger==1:
        break
for k in check:
    print(k)