
def dfs(graph, v, visited):
    visited[v]=True #현재 노드는 방문했으니 True로 설정
    print(v, end=" ")
    for i in graph[v]: #현재 노드와 연결 된 노드를 받는다
        if visited[i]==False: #연결된 노드가 방문처리가 안됨?
            dfs(graph,i,visited) #재귀 함수 실행
#재귀 함수가 핵심인거 같다 ==> 시작점만 주어지면 재귀로 계속 깊게 들어갈 수 있기 때문이다.

graph=[
    [],
    [2,3,8], #1번 노드는 2,3,8번 노드랑 이어져 있다란 의미이다.
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited=[False]*len(graph) # 그래프의 노드 수 만큼! 이걸로 방문 정보를 확인한다.
dfs(graph,1,visited)
