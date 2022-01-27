#https://www.acmicpc.net/problem/17143 백준 17143
import sys ,numpy
from numpy import array

input=sys.stdin.readline


R,C,shark_num=map(int,input().split()) #행,열, 상어수
maze = [[0 for _ in range(C)] for _ in range(R)]
# maze=array(list([[[] for _ in range(C)] for _ in range(R)]))

shark_info1=[]
shark_info2=[]
def fishinh_king(shark_xy,shark_info):
    answer=0
    for i in range(C): #가로 방향으로 끝까지 갈때 기준임.
        #사람이 먼저 움직이고 아래 확인 한 뒤 시작한다.
        # check=numpy.array(maze).T[i]
        # for k in range(len(maze)):
        #     if maze[k][i]!=0:
        #         answer
        print(shark_xy, answer)

        for k in range(len(maze)): #상어의 x,y 정보를 가져와 열이 일치한 부분을 찾는다
            if maze[k][i]!=0:   #만약 maze의 값이 0이 아니라 사람이 있다면
                check=maze[k][i]-1 #maze에는 순서가 적혀있음
                answer+=shark_info[check][2]    #check번째 상어의 크기를 더해줌
                shark_info[check][2]=0 #0으로 크기를 없애버림
                shark_xy[check]=[-1,-1]

                maze[k][i]=0
                break

            # if shark_xy[k][1]==i:#열이 현재 낚시꾼이 있는 i라면
            #     answer+=shark_info[k][2]
            #     maze[shark_xy[k][0]][shark_xy[k][1]]=-1
            #     del shark_xy[k], shark_info[k]
            #     break


        # print(shark_info)
        prev_val=[]
        check_val=[]
        # print(prev_val)
        for j in range(len(shark_xy)):
            shark_speed=shark_info[j][0] #상어의 속도를 빼옴
            if shark_speed==0:

            if shark_info[j][2]==0: #거리정보가 0이면?
                continue


            if shark_info[j][1]==1:          #위로 이동
                dist=shark_xy[j][0]         #dist는 결국 행 or 열의 끝까지 가는데 필요한 거리임
                if dist>=shark_speed: #만약 상어의 이동속도가 행렬을 안 벗어 난다면
                    shark_xy[j][0]-=shark_speed
                else:                   #행 or 열의 끝에 다 도착해도 상어의 이동거리가 남아있다면
                    left_len=shark_speed-dist
                    if left_len<=R-1:
                        shark_xy[j][0]=left_len
                        shark_info[j][1]=2
                        continue
                    val1=left_len//(R-1)
                    val2=left_len%(R-1)
                    if val1%2 ==0: #몫이 2로 나눠진다? 갔다 다시 돌아온거임
                        shark_xy[j][0]=val2
                        shark_info[j][1]=2
                    else:
                        shark_xy[j][0]=(R-1-val2)

            elif shark_info[j][1]==2:       #아래
                dist=(R-1-shark_xy[j][0])       #현재 위치에서 맨 아래로 가는데 필요한 거리
                if dist>=shark_speed:           #상어의 이동거리가 맨 아래로 가는 거리 이하이면
                    shark_xy[j][0]+=shark_speed #걍 더해도됨
                else:
                    left_len=shark_speed-dist #맨 아래로 이동한 거리만큼 상어의 이동 거리를 빼서 남은 거리 찾기
                    if left_len<=R-1:
                        shark_xy[j][0]=R-1-left_len
                        shark_info[j][1]=1
                        continue

                    val1=left_len//(R-1)
                    val2=left_len%(R-1)
                    if val1%2 ==0: #몫이 2로 나눠진다? 갔다 다시 돌아온거임
                        shark_xy[j][0]=(R-1-val2)
                    else:
                        shark_xy[j][0]=val2
                        shark_info[j][1]=1

            elif shark_info[j][1]==3:           #오른쪽
                dist=(C-1-shark_xy[j][1])       #상어의 현재 위치에서 행렬을 벗어나기까지 남은 칸수
                if dist>=shark_speed: #만약 상어의 이동속도가 행렬을 안 벗어 난다면
                    shark_xy[j][1]+=shark_speed
                else:                   #만약 상어의 이동속도가 행렬을 벗어날 정도면
                    # shark_xy[j][1]=(shark_speed-dist)%(C-1)
                    left_len=shark_speed-dist
                    if left_len<=C-1:
                        shark_xy[j][1]=C-1-left_len
                        shark_info[j][1]=4
                        continue
                    val1=left_len//(C-1)
                    val2=left_len%(C-1)

                    if val1%2 ==0: #몫이 2로 나눠 떨어짐? 그럼 왼쪽으로 가야됨
                        shark_xy[j][1]=(C-1-val2)
                        shark_info[j][1] = 4
                    else:
                        shark_xy[j][1]=val2
                        # shark_info[j][1]=4

            elif shark_info[j][1]==4:#왼쪽
                dist = (shark_xy[j][1])             # 상어의 현재 위치에서 행렬을 벗어나기까지 남은 칸수, 왼쪽 이동이니 그냥 자기 위치임
                if dist >= shark_speed:  # 만약 상어의 이동속도가 행렬을 안 벗어 난다면
                    shark_xy[j][1] -= shark_speed
                else:  # 만약 상어의 이동속도가 행렬을 벗어날 정도면
                    # shark_xy[j][1] = (shark_speed - dist) % (C - 1)
                    left_len = shark_speed - dist
                    if left_len<=C-1:
                        shark_xy[j][1]=left_len
                        shark_info[j][1]=3
                        continue
                    val1 = left_len // (C-1)
                    val2 = left_len % (C-1)
                    if val1 % 2 == 0:  # 몫이 2로 나눠 떨어짐? 그럼 오른쪽
                        shark_xy[j][1] = val2
                        shark_info[j][1]=3
                    else:
                        shark_xy[j][1] =(C-1-val2)
        #여기서 갱신된 좌표에 대해 다시 maze를 채워준다.
        prev_val.append([shark_xy[i][0], shark_xy[i][1]])
        if [shark_xy[i][0], shark_xy[i][1]] in prev_val:
            check_val.append([shark_xy[i][0], shark_xy[i][1]])

        #
        # for i in range(len(shark_xy)):
        #     if maze[shark_xy[i][0]][shark_xy[i][1]] ==-1:
        #         maze[shark_xy[i][0]][shark_xy[i][1]]=i #몇번째 값이 들어가 있따.
        #         continue
        #     if (shark_info[maze[shark_xy[i][0]][shark_xy[i][0]]][3]<shark_info[i][3]):
        #         #maze에 들어있던 i번째 순서의 크기 정보를 비교
        #         maze[shark_xy[i][0]][shark_xy[i][1]] = i
        #         del shark_xy[i], shark_info[i]

for i in range(shark_num): #상어의 정보
    r,c,s,d,z=map(int,input().split())

    #r,c는 위치, s는 속도, d는 이동방향, z는 크기(겹치면 크기가 큰게 다먹음)
    #d가 1=위, 2=아래 3=오 4=왼
    maze[r-1][c-1]=i+1
    shark_info1.append([r-1,c-1]) #상어의 좌표값
    shark_info2.append([s,d,z]) #상어의 속도, 이동방향, 크기 정보
# print(maze)
print(shark_info1)
print(shark_info2)
print(maze)
print("여기가 초기 설정값")
fishinh_king(shark_info1,shark_info2)

# for i in maze:
#     print(i)
# print(shark_info1)
# print(shark_info2)
