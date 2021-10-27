import sys
input=sys.stdin.readline
n,m=map(int,input().split())
INF=int(1e9)

#그래프 초기화 과정.
graph=[[INF]*(n+1) for i in range(n+1)]
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0           #자기 자신의 거리는 0이다.

for i in range(m):
    a,b,c=map(int,input().split())
    graph[a][b]=c                   #a에서 b노드로 가는게 c만큼의 거리

#플로이드 워셜 알고리즘 적용
for i in range(1,n+1):              # i번째 간선을 지나간다고 설정함.
    for j in range(1,n+1):
        for k in range(1,n+1):
            graph[j][k]=min(graph[j][k], graph[j][i]+graph[i][k])  #기존에 있던 거리 값, i를 통해 갔을때의 거리값중 작은것을 선택
            #위처럼 해도 상관없는 이유 => 자기 자신을 지나는 point를 0으로 설정했기 때문에 어짜피 자기 자신은 0으로 회귀함.

# 출력
for i in range(1,n+1):
    for j in range(1,n+1):
        print(graph[i][j], end=" ")
    print("")