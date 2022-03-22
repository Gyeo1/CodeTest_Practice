#https://www.acmicpc.net/problem/1149 실버1

#거리에 집이 N개 있음, 집을 R / G / B색으로 칠해야되고 아래 조건을 따르며 최소 비용으로 모든 집을 칠해라
#1) 1번집과 2번집의 색은 반드시 달라야됨
#2) N번집은 N-1 집 색과 달라야됨
#3) i 번집은 i-1,i+1 집의 색과 달라야된다.

n=int(input())

check=[0 for _ in range(n)]
r=[]
g=[]
b=[]
houses=[[] for _ in range(n)]
for i in range(n): # 1~n까지의 집이 R/G/B로 칠할때 드는 비용이다.
    houses[i]=list(map(int,input().split()))
    r.append(houses[i][0])
    g.append(houses[i][1])
    b.append(houses[i][2])
    #r기준으로 잡고 g,b 최소값의 합
check[0]=min(r[0]+min(g[1],b[1]),g[0]+min(r[1],b[1]), b[0]+min(r[1],b[1]))
print(r,g,b)
# check[1]=min(r[1]+min(g[0],b[0])+min(g[2],b[2]),
#              g[1]+min(r[0],b[0])+min(r[2],b[2]),
#              b[1]+min(r[0],g[0])+min(r[2],g[2]))
for i in range(1,n):
    #각 색별로 최소값을 구하는건 맞았는데 구현을 실수했다.
    houses[i][0] = min(houses[i-1][1] , houses[i-1][2])+houses[i][0]
    houses[i][1] = min(houses[i - 1][0], houses[i - 1][2]) + houses[i][1]
    houses[i][2] = min(houses[i - 1][0], houses[i - 1][1]) + houses[i][2]

print(houses)
