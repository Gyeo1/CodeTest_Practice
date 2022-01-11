import sys,heapq
input=sys.stdin.readline

INF=float('inf')
node,lines=map(int,input().split())
graph=[[] for _ in range(node+1)]
#간선 정보가 매우많다==>인접 리스트 사용
def find_way(start,end):
    heap=[]
    dist=[INF]*(node+1)
    dist[start]=0
    heapq.heappush(heap,[0,start]) #시작점은 0의 가중치로 시작
    while heap:
        # print(dist)
        cost,check_node=heapq.heappop(heap)
        for n_node,n_cost in graph[check_node]:
            n_cost+=cost
            if dist[n_node]>n_cost:
                dist[n_node]=n_cost
                heapq.heappush(heap,[n_cost,n_node])

    return dist[end]
for _ in range(lines):
    node1,node2,weigth=map(int,input().split())
    graph[node1].append([node2, weigth])
    graph[node2].append([node1,weigth])
pass1,pass2=map(int,input().split())    #반드시 지나가야되는 구간!

#문제의 핵심!!! ==> pass1과 pass2를 지나는 방법은 1-->pass1-->pass2-->node(마지막 노드)와 1->pass2->pass1->node이다
#즉 1에서 pass1까지 최단거리 pass1부터 pass2까지 최단거리 pass2부터 node까지 최단거리를 더해주면 pass1,2를 지나는 최단거리가 된다
check1=find_way(1,pass1)+find_way(pass1,pass2)+find_way(pass2,node)
check2=find_way(1,pass2)+find_way(pass2,pass1)+find_way(pass1,node)

if check1>=INF and check2>=INF:
    print(-1)
else:
    print(min(check1,check2))
