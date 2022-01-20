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
#아니면 1~n도시 까지 출력 도시 간선이 없으면 해당 도시 -1 출
# import sys
#
# input = sys.stdin.readline
# INF = int(1e9)
#
# # 노드의 개수, 간선의 개수를 입력
# v, e = map(int, input().split())
# # 모든 간선에 대한 정보를 담는 리스트 만들기
# edges = []
# # 최단 거리 테이블을 모두 무한으로 초기화
# distance = [INF] * (v + 1)
#
# # 모든 간선의 정보 입력
# for _ in range(e):
#     a, b, c = map(int, input().split())
#     # a번 노드에서 b번 노드로 가는 비용이 c라는 의미 (a -> b 의 비용이 c)
#     edges.append((a, b, c))
#
#
# def bellman_ford(start):
#     # 시작 노드에 대해서 초기화
#     distance[start] = 0
#     # 전체 v - 1번의 라운드(round)를 반복
#     for i in range(v):
#         # 매 반복마다 '모든 간선'을 확인한다.
#         for j in range(e):
#             cur_node = edges[j][0]
#             next_node = edges[j][1]
#             edge_cost = edges[j][2]
#             # 현재 간선을 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
#             if distance[cur_node] != INF and distance[next_node] > distance[cur_node] + edge_cost:
#                 distance[next_node] = distance[cur_node] + edge_cost
#                 # v번째 라운드에서도 값이 갱신된다면 음수 순환이 존재
#                 if i == v - 1:
#                     return True
#
#     return False
#
#
# # 벨만 포드 알고리즘 수행
# negative_cycle = bellman_ford(1)
#
# # 음수 순환이 존재하면 -1 출력
# if negative_cycle:
#     print("-1")
# else:
#     # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리를 출력
#     for i in range(2, v + 1):
#         # 도달할 수 없는 경우, -1 출력
#         if distance[i] == INF:
#             print("-1")
#         # 도달할 수 있으면 거리 출력
#         else:
#             print(distance[i])력