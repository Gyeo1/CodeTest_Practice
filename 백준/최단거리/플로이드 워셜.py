#플로이드 워셜의 핵심 ==>지나 가는 모든 노드에 대한 최단 거리 측정
import sys
input=sys.stdin.readline
node=int(input())
bus=int(input())
graph=[]
INF=int(1e9)

for _ in range(bus):
    node1, node2, cost= map(int, input().split())
    graph.append((node1,node2,cost))#모든 정보에 대해 저장해야되므로 그대로 저장
print(graph)
def Floyd_warshall(n,graph):
    dist=[[INF] *(n+1) for _ in range(n+1)] #기본 노드 초기화
    for i in range(1,node+1):
        dist[i][i]=0
    for n1,n2,c1 in graph:
        if dist[n1][n2]>c1:#이게 중요한 이유! ==>3중 for문 돌기 전에 최소값 위주로 넣어줘야된다.
            dist[n1][n2]=c1

    for i in range(1,n+1):          #첫번째 for문 거쳐가는 정점
        for j in range(1, n + 1):   #시작 노드
            for k in range(1, n + 1):   #목적지 노드
                #플로이드 워셜의 개념 ==> 시작노드-->목적지 노드로 가는거랑, i를 거쳐서 갔을때를 모두 비교해본다.
                if k != j and dist[j][k] > dist[j][i] + dist[i][k]:
                    dist[j][k] = dist[j][i] + dist[i][k]
                # dist[j][k]=min(dist[j][k],dist[j][i]+dist[i][k])
    print(dist)
Floyd_warshall(node,graph)
