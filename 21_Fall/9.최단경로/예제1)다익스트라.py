import sys
input=sys.stdin.readline
INF=int(1e9)


n,m=map(int, input().split())       #n 노드수 m 간선수.
start=int(input())                  #시작점
graph=[[]for i in range(n+1)]
visited=[False]*(n+1)
distance=[INF]*(n+1)

for _ in range(m):                  #간선의 정보를 받아온다.
    a,b,c=map(int,input().split())   #a번 노드에서 b번 노드로 가는 거리가 c라는 내용이다.
    graph[a].append((b,c))

def next_node():
    value=INF                                   #초기 설정 ==>연결 안되있다!.
    index=0                                     #초기설정
    for i in range(n+1):
        if distance[i]<value and not visited[i]:   #다른 않았고 연결되어 있다면?
            value=distance[i]
            index=i
    return index

def dijkstar(start):
    distance[start]=0
    visited[start]=True
    for i in (graph[start]):        #중요! for문을 이렇게 쓸수 있다는 것을 알아 두자.
        distance[i[0]]=i[1]         #초기 노드 기준으로 연결된 노드이 거리를 초기화 해주기.

    for j in range(n-1):              #여기서 부터 시작임.
        now=next_node()             #다음 노드를 가져옴
        visited[now]=True
        for k in (graph[now]):
            check=distance[now]+k[1]        #중요! 현재 distance가 가지고 있는 값+ 다음 노드 거리
            if check<distance[k[0]]:        #위에서 구한 값이 이미 해당 노드가 가지고 있는 거리 값보다 작으면 갱싱해준다.
                distance[k[0]]=check

dijkstar(start)

print(distance)


