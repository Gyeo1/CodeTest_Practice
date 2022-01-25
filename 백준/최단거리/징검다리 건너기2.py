
#graph를 y축 기준으로 정렬, 그러면 y값에 따른 x값이 들어감, 이걸 기준으로 heapq에 값을 넣어준다?
import heapq, sys
input=sys.stdin.readline

node, final_y=map(int,input().split()) #징검다리 수, 결승선 y좌표
graph=[[] for _ in range(final_y+1)]
INF=float(1e9)
dist = [[] for _ in range(final_y+1)]
def find_way(graph):
    heap=[]
    heapq.heappush(heap,[float(0),0,0]) # cost, x좌표, y좌표 값을 넣는다 초기엔 다 0임
    while heap:
        # print(heap)
        distance, x_point, y_point=heapq.heappop(heap)
        for i in range(-2,3): #-2~2까지의 범위의 y값을 검색
            next_y=y_point+i
            if next_y <0 or next_y>final_y: #y 좌표가 -거나 결승점을 넘어가면 안됨
                continue
            for j in range(len(graph[next_y])):#y 좌표와 연결된 x 좌표를 확인한다.
                next_x=graph[next_y][j]
                # print(next_x, next_y)
                if abs(next_x-x_point)<=2: # 비교 지점이 아니고 x값의 차이가 2이하면
                    next_distacne = ((x_point-next_x)**(2) + (y_point-next_y)**(2))**(0.5)
                    # print(next_x, next_y,x_point,y_point)
                    # print(next_distacne)
                    if dist[next_y][j]> next_distacne+distance and next_distacne>0:
                        dist[next_y][j]=next_distacne+distance
                        heapq.heappush(heap,[next_distacne+distance,next_x,next_y])

start_point=[0,0]
graph[0].append(0)
dist[0].append(0)
for _ in range(node):#노드 갯수만큼 좌표가 주어짐
    x,y=map(int,input().split())#징검다리들의 좌표
    graph[y].append(x) #y좌표와 연결된 x 좌표
    dist[y].append(INF)

# print(dist)
find_way(graph)
# print(dist)
if round(min(dist[-1]))==INF or round(min(dist[-1]))==0:
    print(-1)
else:
    print(round(min(dist[-1])))
    #x,y좌표가 2이하로 차이나는 좌표로만 이동가능하다!

#graph를 y축 기준으로 정렬, 그러면 y값에 따른 x값이 들어감, 이걸 기준으로 heapq에 값을 넣어준다?
#