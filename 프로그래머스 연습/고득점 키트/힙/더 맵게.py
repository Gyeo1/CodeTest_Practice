#https://programmers.co.kr/learn/courses/30/lessons/42626  레벨2

#Question ==> 모든 음식의 스코빌 지수를 K 이상 만들고 싶음, 스코빌 지수가 가장 낮은 두개의 음식을 다음처럼섞는다
#가장 맵지않는 스코빌 지수+(두번째로 맵지않은 스코빌 지수)*2
#K이상의 스코빌 지수를 만들기 위해 섞어야 되는 최소 횟수를 return 하시오

import heapq

def solution(scoville, K):
    check=[]
    answer = 0
    for i in scoville:
        heapq.heappush(check,i)
    while check :
        if check[0]>=K:   #힙큐의 맨 앞은 반드시 최소값임 즉 K보다 크면 break한다.
            break
        a=heapq.heappop(check)
        if a < K and check:         #제일 안 매운값이 K보다 작고 check에 값이 남아있다면 실행
            b=heapq.heappop(check)
            heapq.heappush(check,(a+b*2))   #두개 음식을 섞은 스코빌 지수를 더해준다.
            answer+=1

    if check == []: #힙큐가 비어 있다면 음식을 다 섞어도 K를 넘지 못하는 경우임 -1 return
        return -1
    return answer


# scoville=[1, 2, 3, 9, 10, 12]
scoville=[1,1]
K=7


print(solution(scoville,K))
