#https://programmers.co.kr/learn/courses/30/lessons/42627  Level3

#Question==>디스크는 한번에 한작업만 가능, 디스크 컨트롤러는 요청이 들어오는 순서대로 처리한다
#평균 시간을 가장 줄이는 방법으로 처리하고 걸리는 시간의 평균을 return해라
import heapq, math
def solution(jobs):
    answer = jobs[0][1]+jobs[0][0]      #맨 처음 들어온 작업은 무조건 처리함.
    next_point=jobs[0][1]
    check1=[]
    check2=[]
    for i in range(1,len(jobs)):
        heapq.heappush(check1,[jobs[i][1],jobs[i][0]])
    while check1:
        proccess_time,input_time=(heapq.heappop(check1))
        # print(input_time,proccess_time,next_point)
        if input_time>next_point:



    return math.floor(answer/3)
jobs=[[0, 3], [1, 9], [2, 6]]   #[들어오는 시간, 걸리는 시간]을 나타낸다.
# jobs= [[0, 9], [1, 1], [1, 1], [1, 1], [1, 1]]
print(solution(jobs))
# solution(jobs)