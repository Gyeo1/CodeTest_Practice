T=int(input())
check=[]
for i in range(T):
    a=int(input())
    check.append(a)
d=[0 for i in range(11)]
d[0]=1
d[1]=2
d[2]=4
for j in range(3,11):
    d[j]=d[j-1]+d[j-2]+d[j-3]
for k in check:
    print(d[k-1])

#이 문제 DP이다. 완전 탐색 아님.