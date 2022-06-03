# https://www.acmicpc.net/problem/1520 고르 4
# 참조 자료 https://velog.io/@nathan29849/BAEKJOON-1520-%EB%82%B4%EB%A6%AC%EB%A7%89-%EA%B8%B8-DFS-BFS-python

# 문제: 지도가 주어지면 내리막길로만 이동해서 맨 오른쪽 아래로 이동 가능한 경로의 개수를 return 할것
# 시작점은 0,0 즉 왼쪽 위이다.
# 방향 벡터쓰면 안될꺼같은 느낌? => 메모리 초과 이슈 가능성 多

import sys

sys.setrecursionlimit(10 ** 6)


def dfs(x, y):  #
    global answer
    if x == N - 1 and y == M - 1:  # 현재 좌표가 우측 최 하단이면 종료
        return 1  # 이게 포인트인다 마지막 지점에 도착하면 1을 return하는데 이 1이 dp[y][x]에 더해지는것
    current = maze[y][x]  # 현재 좌표 위치 값
    if dp[y][x] == -1: # -1이면 아직 안지나 갔다는 뜻임.
        dp[y][x] += 1
        # 이렇게 하는 이유? 방향 벡터 쓰면 메모리 초과날꺼 같아서 (500*500이라)
        if -1 < x + 1 < N and maze[y][x + 1] < current:
            dp[y][x] += dfs(x + 1, y)
        if -1 < x - 1 < N and maze[y][x - 1] < current:
            dp[y][x] += dfs(x - 1, y)
        if -1 < y + 1 < M and maze[y + 1][x] < current:
            dp[y][x] += dfs(x, y + 1)
        if -1 < y - 1 < M and maze[y - 1][x] < current:
            dp[y][x] += dfs(x, y - 1)
    return dp[y][x]  # 마지막 부분 외에도 dp[y][x]를 return하는데 -1+1 =0이 return되서 이상한 값이 더해지진않음


M, N = map(int, input().split())
answer = 0
maze = []

# DP를 사용하는 이유? => 모든 경우를 다 따지려면 너무 오래걸림 따라서 dp를 사용해 N-1,M-1에 도착하는 경로에 1을 더하는 방식 사용
dp = [[-1 for _ in range(N)] for _ in range(M)]

for _ in range(M):
    maze.append(list(map(int, input().split())))

dfs(0, 0)
# for i in dp:
#     print(i)
print(dp[0][0])
