import sys,heapq
input=sys.stdin.readline
#서로 다른 두 정점 사이에 여러 개의 간선이 존재할 수도 있음에 유의한다!!
#문제에서 원하는 방식 ==>heapq를 써라 임
INF=float('inf')
def find_weigth(start,graph):

    dist=[INF]*(node+1) #거리의 정보를 담고 있는 리스트 초기에는 아무것도 안 이어졌다고 설정
    heap=[]
    dist[start]=0 #
    heapq.heappush(heap,[0,start]) # 시작 지점의 가중치와 노드를 넣어준다.
    while heap:
        print(heap)
        cost, next_node= heapq.heappop(heap)
        # print(next_node,end =" ")
        for n,c in grape[next_node]:
            c+=cost
            if dist[n]>c:
                dist[n]=c
                heapq.heappush(heap,[c,n])
    return dist


node, lines = map(int,input().split())
start_point=int(input())
# grape={}
grape=[[] for _ in range(node+1)] #인접리스트 사용 (간선 수가 많기 때문이다)
for _ in range(lines):
    node1,node2,weigth=map(int,input().split())
    #문제 해석==> node1에서 node2로만 가는 경우임 즉 5 1 2이면 5-->1은되지만 1-->5는 안된다
    grape[node1].append([node2,weigth]) #인접 리스트에 노드와 가중치 값을 넣는다.
#start_point 기점으로 전체 가중치 구하기
answer=find_weigth(start_point,grape)
# print(answer[node])
# print(grape)
for i in range(1,len(answer)):
    if answer[i] == INF:
        print("INF")
    else:
        print(answer[i])

#다시 풀어볼 문제!
