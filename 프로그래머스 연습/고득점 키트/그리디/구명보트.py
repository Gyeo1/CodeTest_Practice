
def solution(people, limit):
    people.sort()
    count=0
    start=0
    end=len(people)-1
    while start<=end:
        count+=1
        if people[start]+people[end]<=limit: #최소가
            start+=1
        end-=1  #끝에서 부터 지우는 거임
    answer=count

    return answer

people=[70, 80, 50]
# people=[70, 50, 80, 50]
limit=100
print(solution(people,limit))
