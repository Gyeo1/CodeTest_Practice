#미확인 도착지를 풀면서 발견한 방법으로 특정한 최단경로를 다시 풀어보기
import sys,heapq
input=sys.stdin.readline
def find_way(start):
    dist=[int(1e9)] *(node+1)       #cost의 정보
    heap=[]
    dist[start]=0   #시작 지점은 0으로 초기화
    heapq.heappush(heap,[0,start])      #cost, 노드의 정보를 넣어준다.
    while heap:
        check_cost, check_node=heapq.heappop(heap)
        for next_node,next_cost in graph[check_node]:   #그래프에 있는 노드 연결 정보를 가져옴
            next_cost+=check_cost
            if dist[next_node]>next_cost:
                dist[next_node]=next_cost
                heapq.heappush(heap,[next_cost,next_node])
    return dist
node,lines=map(int,input().split())
graph=[[]for _ in range(node+1)]
for _ in range(lines):
    node1,noed2,weigth= map(int,input().split())
    graph[node1].append([noed2,weigth])
    graph[noed2].append([node1,weigth])
path1,path2=map(int,input().split())
start_node=1
#아래가 핵심 다익스트라 3번으로 문제 끝내기!
#문제를 해결하기 위해 start, pass1, pass2를 다익스트라 알고리즘을 돌려서 가중치 정보를 얻는다.
info_start=find_way(start_node)
info_pass1=find_way(path1)
info_pass2=find_way(path2)
#방법은 두가지가 있다 start->pass1->pass2->N까지 가는 방법, start->pass2->pass1->N
# print(info_start,info_pass1,info_pass2)
check_point1=info_start[path1]+info_pass1[path2]+info_pass2[node] #start-->pass1-->pass2-->N
check_point2=info_start[path2]+info_pass2[path1]+info_pass1[node] #start-->pass2-->pass1-->N
if check_point1>=int(1e9) and check_point2>=int(1e9):
    print(-1)
else:
    print(min(check_point1,check_point2)) #둘중 최단 경로를 넣어준다.
# print(info_start[pass2]+info_pass2[pass1]+info_pass1[node])


#문제 1번 노드에서 pass1,pass2를 반드시 지나고 n번 노드로 가는 경우의 수
