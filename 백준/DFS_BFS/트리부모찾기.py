#https://www.acmicpc.net/problem/11725 실버4

# 루트없는 트리가 있는데 루트가 1이라 가정하면 노드의 부모를 구하세요
import sys
sys.setrecursionlimit(10**6)
def dfs(current,array):

    for i in range(len(array[current])):
        next_node=array[current][i]
        if parent[next_node] ==0 and next_node!=1:
            parent[next_node]=current
            dfs(next_node,array)

N = int(input())    # 노드의 개수
check=[[] for _ in range(N+1)]
parent=[0 for _ in range(N+1)]
for _ in range(N-1): #n-1개상의
    node1, node2 = map(int,input().split()) # 서로 연결된 두 정점
    check[node1].append(node2)
    check[node2].append(node1)

dfs(1,check)
for i in range(2,N+1):
    print(parent[i])
# 풀이 방법 => 각 노드의 부모 (즉 자신의 상위에있는 노드)를 찾는 것인데 루트가 1로 고정임
# 즉 루트와 연결된 node를 먼저 확인하고 해당 노드로 부터 연결된 모든 node를 dfs로 탐색