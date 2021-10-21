from collections import deque
#
# N,M =map(int,input().split())
# maze=[]
# for j in range(N):
#     maze.append(list(map(int,input()))) #split안써도 됨
# dy=[-1,1,0,0] #북 서 남 동
# dx=[0,0,-1,1]
#
# # dy=[0,-1,0,1] #북 서 남 동
# # dx=[-1,0,1,0]
#
# def bfs(x,y):
#     queue=deque()
#     queue.append((x,y))
#     while queue:
#         x,y=queue.popleft()
#         for i in range(4):
#             nx=x+dx[i]
#             ny=y+dy[i]
#             if nx<0 or nx>=N or ny<0 or ny>=M:
#                 continue
#             if maze[nx][ny]==0:
#                 continue
#             if maze[nx][ny]==1:
#                 maze[nx][ny]=maze[x][y]+1
#                 queue.append((nx,ny))
#     return maze[N-1][M-1]
#
# print(bfs(0,0))
# # from collections import deque
# #
# # # N, M을 공백을 기준으로 구분하여 입력 받기
# # n, m = map(int, input().split())
# # # 2차원 리스트의 맵 정보 입력 받기
# # graph = []
# # for i in range(n):
# #     graph.append(list(map(int, input())))
# #
# # # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
# # dx = [-1, 1, 0, 0]
# # dy = [0, 0, -1, 1]
# #
# # # BFS 소스코드 구현
# # def bfs(x, y):
# #     # 큐(Queue) 구현을 위해 deque 라이브러리 사용
# #     queue = deque()
# #     queue.append((x, y))
# #     # 큐가 빌 때까지 반복하기
# #     while queue:
# #         x, y = queue.popleft()
# #         # 현재 위치에서 4가지 방향으로의 위치 확인
# #         for i in range(4):
# #             nx = x + dx[i]
# #             ny = y + dy[i]
# #             # 미로 찾기 공간을 벗어난 경우 무시
# #             if nx < 0 or nx >= n or ny < 0 or ny >= m:
# #                 continue
# #             # 벽인 경우 무시
# #             if graph[nx][ny] == 0:
# #                 continue
# #             # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
# #             if graph[nx][ny] == 1:
# #                 graph[nx][ny] = graph[x][y] + 1
# #                 queue.append((nx, ny))
# #     # 가장 오른쪽 아래까지의 최단 거리 반환
# #     return graph[n - 1][m - 1]
# #
# # # BFS를 수행한 결과 출력
# # print(bfs(0, 0))

#1은 이동가능 경로 0은 괴물이 있는 부분. 최소 경로? ==>목적지 도착할때 까지 칸을 1씩 증가하면된다?
N,M=map(int, input().split())
maze=[]
for i in range(N):
    maze.append(list(map(int,input())))

dx=[-1,1,0,0] #상 하 좌 우
dy=[0,0,-1,1] #상 하 좌 우
def bfs(x,y):
    queue=deque()
    queue.append((x,y)) #현재 좌표를 입력

    while queue:
        x,y=queue.popleft()
        for i in range(4): #상 하 좌 우 체킹
            nx=dx[i]+x
            ny=dy[i]+y

            if nx<0 or nx>=N or ny>=M or ny<0: #인덱스 범위에서 벗어나면
                continue#다음 반복문이로!

            if maze[nx][ny]==1:
                maze[nx][ny]=maze[x][y]+1
                queue.append((nx,ny))

    return maze[N-1][M-1]
print(bfs(0,0))