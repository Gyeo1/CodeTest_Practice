import sys
import heapq

input=sys.stdin.readline
INF=int(1e9)
n,m=map(int,input().split())
start=int(input())
distance=[INF]*(n+1)
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a , b, c=map(int,input().split())         #a노드와 연결된 b노드의 거리는 c이다.
    graph[a].append((b,c))

def dijkstra(start):
    distance[start]=0
    Q=[]                                    #우선순위 큐를 사용할 리스트 초기화
    heapq.heappush(Q,(0,start))             #현재 시작점의 거리는 0을 의미한다.
    while Q:                                #큐가 비어있을때 까지 실행 ==> 비었다면 탐색이 끝났다는 의미!
        dist, index=heapq.heappop(Q)        #우선 순위 큐에서 거리와, 인덱스에 대한 정보를 꺼내온다.
        if distance[index]<dist:            #만약 이전에 다른 곳이 지나가서 distance값이 dist 미만이라면 이미 최소값이니깐 실행 x
            continue
        for i in graph[index]:              #현재 노드와 연결된 노드 정보를 받는다.
            cost=dist+i[1]                  #연결된 노드와의 거리 측정
            if cost<distance[i[0]]:         #거리가 기존 노드에 저장된 거리보다 작다면? 갱신!
                distance[i[0]]=cost
                heapq.heappush(Q,(cost,i[0]))
dijkstra(start)
print(distance)

