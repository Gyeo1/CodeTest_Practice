#https://programmers.co.kr/learn/courses/30/lessons/42627  Level3

#Question==>디스크는 한번에 한작업만 가능, 디스크 컨트롤러는 요청이 들어오는 순서대로 처리한다
#평균 시간을 가장 줄이는 방법으로 처리하고 걸리는 시간의 평균을 return해라
import heapq, math


def solution(jobs):

    check=[]
    count=0
    pre_point= -1
    next_point= 0
    answer=next_point
    while count<len(jobs):
        for i in range(len(jobs)):
            if pre_point<jobs[i][0]<=next_point:       #pre_point는 이전에 처리한 작업의 시작 시간대, next는 끝난 시간대
                #즉 한 작업을 수행하는동안 실행되었던 proceess를 찾는 다는 의미이다.
                heapq.heappush(check,[jobs[i][1],jobs[i][0]])
        print(check,pre_point,next_point)
        if check: #힙큐의 값을 처리하면서 pre_point와 next_point값을 바꿔준다.
            proccess=heapq.heappop(check)
            pre_point=next_point
            next_point+=proccess[0]
            answer+=(next_point - proccess[1])
            count+=1
        else:
            next_point+=1
    return math.floor(answer/len(jobs))


jobs=[[0, 3], [1, 9], [2, 6]]   #[들어오는 시간, 걸리는 시간]을 나타낸다.
# jobs= [[0, 9], [1, 1], [1, 1], [1, 1], [1, 1]]
print(solution(jobs))
