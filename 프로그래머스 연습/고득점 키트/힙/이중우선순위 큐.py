#https://programmers.co.kr/learn/courses/30/lessons/42628      레벨3

#질문 ==> 이중 순위 우션 큐는 다음 연산을 할 수 있는 자료 구조임
#명령) I 숫자=> 큐에 주어진 숫자를 삽입
#명령) D 1 ==> 최대 값을 삭제한다.
#명령) D -1 ==> 최소값을 삭제한다
#이중 우선순위 큐가 할 연산이 매개 변수로 주어질때 모든 연산을 처리하고 나서 큐의 [최대, 최소] 형태로 return하도록 해라
#만약 비어있으면 [0,0]을 return

import heapq
def solution(operations):

    heap1=[]        #최소 값을 넣을 힙
    heap2=[]        #최대 값을 넣을 힙
    for i in operations: #Operations 작업 처리
        check=i.split()  # 명령과 값 분리
        check[1]=int(check[1])
        print(check,heap1,heap2)

        if check[0]=='I':
            if heap1==[]:       #최소힙에 아무 값도 없으면 최소힙에 값을 넣는다. 항상 최소 힙을 맨처음에 넣는다
                heapq.heappush(heap1,check[1])
                continue

            if check[1]<= heap1[0]:  #삽입값이 최소 값 보다 작으면?
                heapq.heappush(heap2,-(heapq.heappop(heap1))) #최소값을 최대 힙에 넣어주고 최소값을 최소 힙에 넣는다
                heapq.heappush(heap1,check[1])

            elif check[1]>= heap1[0]: #삽입값이 최소값보다 크면 삽입 값을 최대 힙쪽으로 넣어준다.
                if heap2==[]:
                    heapq.heappush(heap2, -check[1])
                    continue
                if check[1]>= -(heap2[0]) :
                    heapq.heappush(heap1,-(heapq.heappop(heap2)))
                    heapq.heappush(heap2,-(check[1]))
            else:
                heapq.heappush(heap1, check[1])
        elif check[0]=='D' and check[1]==1: #최대값 삭제
            if heap2: #최대 힙을 pop
                heapq.heappop(heap2)
            elif heap1:#만약 최대 힙이 없으면 최소힙 값을 지운다
                heapq.heappop(heap1)

        elif check[0]=='D' and check[1]==-1: #최소 값 삭제
            if heap1:
                heapq.heappop(heap1)
            elif heap2:
                heapq.heappop(heap2)
    # print(heap1,heap2)
    if heap1==[] and heap2==[]:
        return [0,0]
    elif heap1 and heap2:
        return [-(heapq.heappop(heap2)), heapq.heappop(heap1)]
    elif heap1 and heap2==[]:
        return [heapq.heappop(heap1),heapq.heappop(heap1)]
    elif heap1==[] and heap2:
        return [-(heapq.heappop(heap2)),-(heapq.heappop(heap2))]

    # return answer

# operation=["I 16","D 1"]
# operation=["I 7","I 5","I -5","D -1"]
# operation=["I 16","I -5643", "D -1", "D 1","D 1", "I 123 ", 'D -1' ]
operation=["I -45","I 653", "D 1",'I -642', "I 45","I 97", "D 1 ", 'D -1',"I 333" ]
print(solution(operation))
