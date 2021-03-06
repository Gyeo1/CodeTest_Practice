#연결이 안된 노드는 INF로 표현
INF=999999999
#인접 행렬 방식
graph=[
    [0,7,5], #0번 노드의 간선, 자기 자신 인덱스는 0으로!
    [7,0,INF], #1번 노드의 간선
    [5,INF,0] #2번 노드의 간선
]



#인접 리스트 방식 ==> 각 노드의 연결 정보를 하나씩 APPEND 시켜준다.
# 연결리스트라는게 필요한데 파이썬은 자체 적으로 append 제공!

graph_2=[[] for _ in range(3)] #2차원 리스트로 초기화

#0번 노드의 연결도 표현
graph_2[0].append((1,7)) #1번 노드와 7의 가중치 간선으로 연결
graph_2[0].append((2,5)) #2번 노드와 5의 가중치 edge로 연결

#1번 노드의 연결도 표현
graph_2[1].append((0,7)) #0번 노드와 7가중치 edge로 연결

#2번 노드의 연결도 표현
graph_2[2].append((0,5)) #0번 노드와 5가중치로 연결

print(graph)
print(graph_2)