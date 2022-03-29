#https://www.acmicpc.net/problem/1149 실버1

#거리에 집이 N개 있음, 집을 R / G / B색으로 칠해야되고 아래 조건을 따르며 최소 비용으로 모든 집을 칠해라
#1) 1번집과 2번집의 색은 반드시 달라야됨
#2) N번집은 N-1 집 색과 달라야됨
#3) i 번집은 i-1,i+1 집의 색과 달라야된다.

N=int(input())
houses=[]
check=[[0,0,0] for _ in range(N)]
for _ in range(N):
    houses.append(list(map(int,input().split())))
check[0]=houses[0]
for i in range(1,N):
    #1부터는 각각 R을 골랐을때 이전의 B,G중 최소값을 선택하는 방식으로 진행한다
    check[i][0]=houses[i][0]+min(check[i-1][1],check[i-1][2])
    check[i][1]=houses[i][1]+min(check[i-1][0],check[i-1][2])
    check[i][2]=houses[i][2]+min(check[i-1][1],check[i-1][0])

print(min(check[N-1]))