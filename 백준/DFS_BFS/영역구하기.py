# https://www.acmicpc.net/problem/2583 실버1
import sys

sys.setrecursionlimit(10 ** 6)


def dfs(x, y):
    global area
    maze[y][x] = 1  # 현재 좌표 값을 1로 설정
    area += 1  # 넓이를 +1 해줌
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < nx < N and -1 < ny < M and maze[ny][nx] == 0:  # 인접한 곳이 연결되면 dfs 실행
            dfs(nx, ny)


M, N, K = map(int, input().split())  # M,K 는 좌표(Map)이고 K는 직사각형의 좌표의 수
maze = [[0 for _ in range(N)] for _ in range(M)]
check = []
for _ in range(K):
    check.append(list(map(int, input().split())))
for i in range(len(check)):
    x_1, y_1, x_2, y_2 = check[i][0], check[i][1], check[i][2], check[i][3]
    for j in range(min(y_1, y_2), max(y_1, y_2)):
        for k in range(min(x_1, x_2), max(x_1, x_2)):
            maze[j][k] = 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = []

for i in range(len(maze)):
    while 0 in maze[i]: # 중요*) 각 행에서 0인 부분이 사라질때까지 반복한다는 의미,
        # 예전처럼 전체 while 묶을 필요가 없으므로 더 좋은 알고리즘이다
        area = 0
        dfs(maze[i].index(0), i)  # maze에서 0인 부분 좌표를 찾아서 dfs 실행
        result.append(area)
result.sort()
print(len(result))
for i in result:
    print(i, end=" ")
