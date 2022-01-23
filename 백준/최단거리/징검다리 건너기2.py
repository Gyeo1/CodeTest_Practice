import heapq, sys
input=sys.stdin.readline

node, final_y=map(int,input().split()) #징검다리 수, 결승선 y좌표
graph=[[] for _ in range(final_y+1)]
INF=int(1e9)
def find_way(graph):
    dist=[INF]*(final_y)
    dist[0]=0
    heap=[]
    heapq.heappush(heap,[0,0]) #y좌표가 0이면 0으로 시작
    while heap:
        distance, y_point=heapq.heappop(heap)
        for
    return

start_point=[0,0]
graph[0].append(0)
for _ in range(node):#노드 갯수만큼 좌표가 주어짐
    x,y=map(int,input().split())#징검다리들의 좌표
    graph[y].append(x) #y좌표와 연결된 x 좌표
# graph.sort()
print(graph)
    #x,y좌표가 2이하로 차이나는 좌표로만 이동가능하다!