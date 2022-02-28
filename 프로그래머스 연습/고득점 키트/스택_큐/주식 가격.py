#https://programmers.co.kr/learn/courses/30/lessons/42584 레벨2

#Question ==> 초단위로 기록된 주식 가격 == price
#             가격이 떨어지지 않는 기간은 몇 초인지 return하시오

from collections import deque
def solution(prices):
    deq1=deque()
    count=0
    check=[-1 for _ in range(len(prices))]
    deq1.append((prices[0],0))
    for i in range(1,len(prices)):
        count += 1
        if deq1[-1][0]>prices[i]:
            while deq1 and deq1[-1][0]>prices[i]:
                print("떨어진 기간 발생", deq1[-1])
                check[deq1[-1][1]]=abs(deq1[-1][1]-(count))
                deq1.pop()


        deq1.append((prices[i],i))
        print(deq1, prices[i])

    for j in range(len(check)):

        if check[j] == -1:
            check[j]=(count)
        count-=1



    return check


price=[1,2,3,2,3]
print(solution(price))