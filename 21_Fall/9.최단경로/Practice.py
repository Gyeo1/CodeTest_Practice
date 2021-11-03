import heapq
import sys
#다익 스트라는 시작점을 기준으로 시작점이 다른 노드로 가는데 필요한 최소 경로를 찾는데 사용한다.

INF=1000000000
input=sys.stdin.readline
n,m=map(int,input().split())
start=int(input())
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)
for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c))

def dijk(start):
    distance[start]=0                   #시작 지점은 0으로 초기화
    Q=[]
    heapq.heappush(Q,(0,start))         #우선 순위 큐에 시작지점의 인덱스와 거리를 넣어줌
    while Q:
        length,node= heapq.heappop(Q)
        if length<distance[node]:           #저장되어 있던 거리 정보가 더 작다? ==>이미 한번 지나간 node이다.
            continue
        for i in graph[node]:               #현재 노드와 연결된 다른 노드들의 정보를 하나씩 가져온다
            cost= distance[node]+i[1]       #현재 노드의 distance와 연결된 다른 노드의 거리를 더해준다
            if cost<distance[i[0]]:         # 해당 값이 연결된 노드가 가지고 있는 거리 정보 보다 작으면 갱신
                distance[i[0]]=cost
                heapq.heappush(Q,(cost,i[0]))   #갱신된 노드의 정보를 넣어준다.

dijk(start)
for i in range(1,n+1):
    print(distance[i])