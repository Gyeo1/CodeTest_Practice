from collections import deque
deq=deque()
def solution(priorities, location):
    count=0
    for i in priorities:
        deq.append(i)
    while 1:
        check = max(deq)
        a=deq.popleft()
        if a==check: #우선순위 1등?
            count+=1
            if location==0:
                answer=count
                break
            else:
                location-=1
        elif a<max(deq):
            deq.append(a)
            if location==0:
                location=len(deq)-1
            else:
                location-=1
    return answer

priorities=[2, 1, 3, 2]
location=3
print(solution(priorities,location))