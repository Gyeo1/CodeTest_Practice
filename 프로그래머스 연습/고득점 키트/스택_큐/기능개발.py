#https://programmers.co.kr/learn/courses/30/lessons/42586 level2

#Question: 기능 개선작업중인데 각 기능은 진도가 100이여야 서비스 반영가능
#앞의 기능보다 뒤의 기능 개선이 먼저 일어날 수 있다. 이때 앞의 기능이 배포되기 전까지 기다려야됨
#작업 진도와 speed가 정해졌을때 배포마다 몇개씩 배포되는지 구해라

from collections import deque

def solution(progresses, speeds):
    answer = []
    deq1=deque(progresses)
    while deq1:
        for i in range(len(deq1)):
            if deq1[i] <100:
                deq1[i]+=speeds[i]

        if deq1[0]>=100:
            count = 0
            while deq1 and deq1[0] >=100:
                deq1.popleft()
                del speeds[0]       #deq와 연동되는 speed 값 지우기
                count+=1
            answer.append(count)

    return answer



progresses=[93, 30, 55]
speed=	[1, 30, 5]
# progresses=[95, 90, 99, 99, 80, 99]
# speed=	[1, 1, 1, 1, 1, 1]
print(solution(progresses,speed))