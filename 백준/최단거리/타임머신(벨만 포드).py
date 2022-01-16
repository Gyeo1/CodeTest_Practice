import sys

input=sys.stdin.readline

#문제 N개 도시가 있다(node), 버스는 M개가 있다(Line) 가중치가 음수면 타임머신!
#가중치가 0이면 순간 이동, 음수면 타임머신 1 번도시에서 나머지 도시로 가는 빠른시간 구해라
INF=int(1e9)

node, lines=map(int,input().split())
graph=[]
dist=[INF]*(node+1)
for _ in range(lines):
    node1, node2, cost= map(int, input().split())
    graph.append((node1,node2,cost))
strat_node=1

def bellman_ford(start):
    dist[start]=0
    for i in range(node):
        for j in range(lines):
            current_node=graph[j][0]
            next_node=graph[j][1]
            next_cost=graph[j][2]
            if dist[current_node] != INF and dist[next_node]>dist[current_node]+next_cost:
                dist[next_node]=dist[current_node]+next_cost
                if i==node-1:
                    return True
    return False
check=bellman_ford(strat_node)

if check:
    print('-1')
else:
    for k in range(2,node+1):
        if dist[k]== INF:
            print('-1')
        else:
            print(dist[k])
#출력=>만약 어떤 도시가 무한 루프에 빠진면 -1
#아니면 1~n도시 까지 출력 도시 간선이 없으면 해당 도시 -1 출력