from collections import deque
def solution(progresses, speeds):
    deq=deque()
    deq2=deque()
    answer = []
    for i in range(len(progresses)):
        deq.append(progresses[i])#deq에다 넣어주기
        deq2.append(speeds[i])
    while deq:
        check = 0
        for i in range(len(deq2)):
            deq[i]+=deq2[i]
        while deq and deq[0]>=100 :
            check+=1
            deq.popleft()
            deq2.popleft()
        if check!=0:
            answer.append(check)
    return answer

progresses=[93, 30, 55]
speed=[1, 30, 5]
print(solution(progresses,speed))
#Progresses는 현재 진행중인상황  Speed는 하루당 처리량이다.
#2번째 작업이 완료 되더라도 첫번째 작업이 끝나지않으면 배포되지 못한다.
