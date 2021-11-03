import sys

input=sys.stdin.readline
INF=int(1e9)
N,M=map(int,input().split())
graph=[[INF]*(N+1) for _ in range(N+1)]     #초기화 전부 안 이어져있다고 가정
for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j:
            graph[i][j]=0

for _ in range(M):
    a, b=map(int,input().split())
    graph[a][b]=1                   #모든 도로의 거리는 1이다.
    graph[b][a]=1                   #양방향 통행이 가능?

X,K=map(int,input().split())        #K를 들렸다 X로 가는것이 목표!

for i in range(1,N+1):
    for j in range(1,N+1):
        for k in range(1,N+1):
            graph[j][k]=min(graph[j][k],graph[j][i]+graph[i][k])

# for i in range(1,N+1):
#     for j in range(1,N+1):
#         print(graph[i][j],end=" ")
#     print("")
#
result=graph[1][K]+graph[K][X]
if result<INF:
    print(result)
else:
    print(-1)