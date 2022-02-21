# https://www.acmicpc.net/problem/16173     실버 5문제

import sys
sys.setrecursionlimit(10**6)
check=0
def dfs(point_0,point_1):
    global check,size,maze
    move_point=maze[point_0][point_1]
    if move_point==-1:
        check=1
        return
    elif move_point==0:         #어짜피 0 기준이면 아무것도 못하니 return(**메모리 초과 이슈)
        return
    if point_0+move_point<size and check==0:
        # print(point_0+move_point,point_1)
        dfs(point_0+move_point,point_1)
    if point_1+move_point<size and check==0:
        # print(point[0], point[1]+move_point)
        dfs(point_0,point_1+move_point)

size=int(input())
maze=[]

for _ in range(size):
    a=map(int,input().split())
    maze.append(list(a))

dfs(0,0)
if check==1:
    print('HaruHaru')
else:
    print("Hing")
