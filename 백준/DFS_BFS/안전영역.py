#https://www.acmicpc.net/problem/2468  실버1문제

#문제: 높이 정보가 주어졌을때 안전 영역의 최대 개수를 계산하는 프로그램 작성
# def dfs2()
import copy,sys
sys.setrecursionlimit(10**6)
def dfs(y,x):
    global check_maze
    check_maze[y][x]=0            #해당 좌표를 도착하면 0으로 바꿔줌

    #아래는 상 하 좌 우에서 이동할 수 있는 공간을 찾는 방법임.
    if x+1<N and check_maze[y][x+1]!=0:
        dfs(y,x+1)
    if x-1>=0 and check_maze[y][x-1]!=0:
        dfs(y,x-1)
    if y+1<N and check_maze[y+1][x]!=0:
        dfs(y+1,x)
    if y-1>=0 and check_maze[y-1][x] !=0:
        dfs(y-1,x)


answer=1 #안잠길수 있으니 1로
N=int(input())
graph=[]
max_hegith=0
min_hegith=100              #최대 높이는 100이니깐

for i in range(N):
    a=map(int,input().split())
    graph.append(list(a))       #높이 정보를 리스트로 저장
    check_1=max(graph[i])
    check_2=min(graph[i])
    if max_hegith<check_1:  #최대 높이 찾기
        max_hegith=check_1
    if min_hegith>check_2:  #최소 높이 찾기
        min_hegith=check_2

#문제 풀이 접근 방법 ==>1)최소 높이~최대 높이까지 1씩늘리면서 해당 높이에 속하는 지역을 '0'으로 만들어준다
#2) 반복문으로 graph에서 0이 아닌 부분을 찾는다.
#3) 해당 부분에서 dfs 실행 ==> dfs는 시작지점에서부터 0이 아닌 부분을 찾아 0으로 만들어준다(전부)
for j in range(min_hegith,max_hegith+1):

    for k in range(len(graph)):#그래프를 돌면서 j값 즉 지울 높이를 찾는다
        while 1:
            if j in graph[k]:  #j가 graph에 있으면 해당 인덱스를 0으로 지워라
                idx=graph[k].index(j)
                graph[k][idx]=0
            else:
                break
    # print(graph)
    check_maze=copy.deepcopy(graph) #깊은 복사로 내용 복사
    # print(check_maze)
    number=0

    #
    for l in range(len(check_maze)):
        for m in range(len(check_maze[l])):
            if check_maze[l][m]!=0:
                dfs(l,m)
                number+=1

    answer=max(number,answer)
print(answer)