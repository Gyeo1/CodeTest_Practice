N= int(input())
check=[]
for i in range(N):
    check.append(int(input()))
check.sort()
for i in range(N-1,-1,-1):
    print(check[i], end=" ")

#check=sorted(check, reverse=True)로 하는 방법이 정석?