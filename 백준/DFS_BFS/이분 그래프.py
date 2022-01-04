import sys
from collections import deque
input=sys.stdin.readline
test_case=int(input())
def bfs(graph):
    keys=sorted(list(graph.keys()))
    start=keys[0] # 맨 첫번째 값을 가져옴.
    queue=deque()
    queue.append(start)
    left_side=set([])
    rigth_side=set([])
    left_side.add(start)
    visited=[False]*(node+1)
    while graph:
        if len(queue)==0:
            #만약 큐가 비었다 ==> 모든 노드끼리 연결이 안된상태, 다른 노드를 찾아야된다.
            queue.append(list(graph.keys())[0]) #이게 가능한 이유 이미 앞에 관련된 노드는 다 지워버려서 새 노드와 관련된거만 남음
            left_side.add(list(graph.keys())[0])#left쪽에 추가해줌
        idx=queue.popleft()
        # print(idx,end=" ")
        visited[idx]=True
        for i in graph[idx]: #graph는 딕셔너리이므로 graph[key]를 넣으면 items가 나온다.
            if idx in left_side and(i not in rigth_side):
                if i in left_side:
                    print("NO")
                    return
                rigth_side.add(i)

            elif idx in rigth_side and (i not in left_side):
                if i in rigth_side:
                    print("NO")
                    return
                left_side.add(i)

            if visited[i]==False:#큐에 다음 노드를 추가하는 과정
                queue.append(i)
                visited[i]=True
        del graph[idx]#한번 확인한 그래프는 걍 지워버림
    # print(left_side,rigth_side)
    print("YES")




for _ in range(test_case):
    node,lines=map(int,input().split())
    graph={}
    #인접 리스트 방식으로 graph 구현 ==> 왜냐면 노드의 갯수가 20000일시 인접 행렬 방식은 20000*20000으로 메모리낭비가 너무 심하다
    #인접 리스트는 인접 행렬보다 구현이 힘들지만 시간과 메모리 절약이 되므로 노드 갯수가 많으면 인접 리스트를 쓰자
    for _ in range(lines):
        x,y=map(int,input().split())
        if x not in graph.keys():
            graph[x]=set([y])
        else:
            graph[x].add(y)
        if y not in graph.keys():
            graph[y]=set([x])
        else:
            graph[y].add(x)
    # print(graph)
    bfs(graph)