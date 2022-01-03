#수빈이는 동생과 숨바꼭질을 한다. 수빈이는 걷거나 순간이동이가능 걸을때는 +-1만큼 이동, 순간이동은 *2의 위치로 이동
from collections import deque
N,K=map(int,input().split()) #N은 수빈이가 있는 위치 K는 동생의 위치
queue=deque() #큐에 모든 경우의 수를 넣어주기 위함
# graph=[0 for _ in range(max(N,K)*2)]
# if K*2<100000:
#     graph=[0 for _ in range(max(N,K)*2)]
# else:
#     graph = [0 for _ in range(max(N, K) +1)]
graph = [-1 for _ in range(100010)] #항상 최대의 값을 가지도록 설정
graph[N]=0

#bfs로 수빈이의 위치에서 K까지 도달 가능한 경우의 수를 모두 계산?

def bfs(start,end):
    global graph
    K=end
    queue.append(start)
    while queue:
        N=queue.popleft()
        if N<0 or N>len(graph):
            continue
        # print(N, graph[N])
        if N>K: #도착지점이 뒤에 있다면 -1해준다.
            if graph[N-1]>graph[N]+1 or graph[N-1]==-1:
                graph[N-1]=graph[N]+1
                queue.append(N-1)

        if N*2<=100000 :
            if graph[N*2]==-1:
                graph[N * 2] = graph[N] + 1
                queue.append(N * 2)
            elif graph[N*2]>graph[N]+1:
                #이게 뭘 의미? 이미 최소의 값을 가지고 있다면 큰값을 안받기 위한 장치.
                # print(N*2, graph[N])
                graph[N*2]=graph[N]+1
                queue.append(N*2)

        if N+1<=K :
            # if  graph[N+1]==0:
            #     graph[N + 1] = graph[N] + 1
            #     queue.append(N + 1)
            if (graph[N + 1] > graph[N] + 1) or graph[N+1]==-1:
                graph[N+1]=graph[N]+1
                queue.append(N+1)
        if N-1<=K :
            # if graph[N-1]==0:
            #     graph[N - 1] = graph[N] + 1
            #     queue.append(N - 1)
            if (graph[N-1]>graph[N]+1) or graph[N-1]==-1:
                graph[N-1]=graph[N]+1
                queue.append(N-1)
bfs(N,K)
# print(graph[])
# print(graph[:K+10])
print(graph[K])