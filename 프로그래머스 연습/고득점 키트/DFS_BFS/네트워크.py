#https://programmers.co.kr/learn/courses/30/lessons/43162 레벨3

#Question: 컴퓨터 갯수 n 연결에 대한 정보 computers가 매개 변수로 주어질때 네트워크의 개수를 return
#network란 서로 연결되어 있는 하나의 컴퓨터 집합? 임
#자기자신은 항상 1이고 연결안된건 0이다
def dfs(start,computers):
    global visited
    visited[start]=True
    print(visited)
    for i in range(len(computers[0])):
        if i != start and computers[start][i]==1 and visited[i]==False:
            dfs(i,computers)

    return
def solution(n, computers):
    global visited
    visited=[False for _ in range(n)]
    answer = 0
    for i in range(n):         #첫번째 노드 부터 n번째 노드 정보를 확인한다

        for j in range(n):      #자기 자신과 연결된 노드 정보를 가져와 처리한다
            if computers[i][j]==1 and visited[j]==False:
                visited[i] = True # computers 값이 1이고 visited가 false면 방문처리
                print(i,j,visited)
                dfs(j,computers)
                answer+=1

    return answer
# n=3
# computers=[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# computers=[[1, 1, 0], [1, 1, 1], [0, 1, 1]]
n=4
computers= [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 1, 0, 1]]
visited=[False for _ in range(len(computers[0]))]
print(solution(n,computers))
