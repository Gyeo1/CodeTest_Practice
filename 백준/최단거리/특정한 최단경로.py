import sys,heapq
input=sys.stdin.readline

INF=float('inf')
node,lines=map(int,input().split())
graph=[[] for _ in range(node+1)]
#간선 정보가 매우많다==>인접 리스트 사용
def find_way(graph):
    heap=[]
    dist=[[INF,0] for _ in range(node+1)]

    dist[1][0]=0 #맨 처음 노드값은 0으로 설정
    heapq.heappush(heap,[0,1,0]) #cost=0 , 시작 node=1,flags=0으로 설정
    print(dist)
    dist[1][0]=INF
    while heap:
        cost,current_node,flags=heapq.heappop(heap)
        for n_node,n_cost in graph[current_node]:
            n_cost+=cost
            #만약 반드시 지나가야되는 곳이 다음 노드다 ==> heap의 flags에 다른 값을 넣어준다.
            #만약pass1이 다음 노드임,근데flags=0 즉 이전까지 한번도 pass 노드를 안지났다면 pass1을 넣어줌
            #근데 pass2를 지나고 나서 pass1을 만난거라면 3을 넣어줌 3인 상태에서는 아무도 못막음
            #마찬가지로 pass2도 pass1을 지나면서 왔는지 아닌지를 판단한다.


            if flags==3:#flag가 3이면 이미 모든 필수 노드를 지나왔다는 거다
                #만약 flasg=3 즉 필수노드를 지나왔는데 dist[node][1]의 값이 0이면 필수노드를 지난 값이 우선이므로 필수노드 값을 넣어준다
                if dist[n_node][1]==0:
                    dist[n_node][0]=n_cost
                    dist[n_node][1]=1
                    heapq.heappush(heap, [n_cost, n_node, flags])
                    continue
                else:
                    #만약 flags=3인데 dist에 들어있는 값도 flags의 3이였을때 값이면 값을 비교해 준다.
                    if dist[n_node][0] > n_cost:
                        dist[n_node][0] = n_cost
                        heapq.heappush(heap, [n_cost, n_node, flags])
                        continue

            if n_node==pass1:
                if flags==0:
                    heapq.heappush(heap,[n_cost,n_node,pass1])
                # elif flags==pass1: #이건 뭐냐 왔다가 다시 올아오는 경우이다. 이러면 무조건 값이 클수밖에없음

                elif flags==pass2:
                    dist[n_node][0]=n_cost
                    dist[n_node][1]=1
                    heapq.heappush(heap,[n_cost,n_node,3])
            elif n_node==pass2:
                if flags==0:
                    heapq.heappush(heap,[n_cost,n_node,pass2])
                elif flags==pass1:
                    heapq.heappush(heap,[n_cost,n_node,3])

            if dist[n_node][0] > n_cost and dist[n_node][1]==0:#
                dist[n_node][0] = n_cost
                heapq.heappush(heap, [n_cost, n_node, flags])
        print(heap)
    return dist


for _ in range(lines):
    node1,node2,weigth=map(int,input().split())
    graph[node1].append([node2, weigth])
    graph[node2].append([node1, weigth])
pass1,pass2=map(int,input().split())    #반드시 지나가야되는 구간!
print(graph)
print(find_way(graph))