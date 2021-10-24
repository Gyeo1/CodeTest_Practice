N= int(input())
check=[]
for i in range(N):
    check.append(int(input()))
check.sort()
for i in range(N-1,-1,-1):
    print(check[i], end=" ")

#아래 둘처럼 하는게 정석이긴하다.
#check=sorted(check, reverse=True)
# check.sort(reverse=True)