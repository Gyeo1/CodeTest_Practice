import sys
input=sys.stdin.readline
INF=int(1e9)
n,m=map(int,input().split())
graph=[[INF]*(n+1) for _ in range(n+1)]         #플로이드 워셜은 2차원 리스트를 필요로한다.


for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0
for i in range(m):                              #간선 정보 입력
    a, b, c = map(int, input().split())
    graph[a][b]=c

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            graph[j][k]=min(graph[j][k], graph[j][i]+graph[i][k])
