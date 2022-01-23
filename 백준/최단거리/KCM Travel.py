import sys,heapq

input=sys.stdin.readline
INF=int(1e9)
test_case=int(input())
def find_way(graph):
    print(total_cost)
    heap=[]
    dist=[[INF for _ in range(node+1)] for _ in range(node+1)]

for _ in range(test_case):
    node, total_cost, ticket=map(int,input().split())
    graph=[[] for _ in range(node+1)]
    for _ in range(ticket):
        node1, node2, cost, time=map(int,input().split())
        graph[node1].append([node2,cost,time])
        # graph[node2].append([node1,cost,time])

    check=(find_way(graph))
    print(check)
    # if check[-1] !=INF:
    #     print(check[-1])
    # else:
    #     print("Poor KCM")
