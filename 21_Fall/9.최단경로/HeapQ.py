import heapq

def heapsort(iterable):
    array=[]
    result=[]
    for value in iterable:
        heapq.heappush(array,value) #array에 매개변수로 받은 값들을 넣어 준다,
    for i in range(len(array)):
        result.append(heapq.heappop(array))     #array에 있는 값을 heappop시켜준다.
    return result

print(heapsort([1,3,5,7,9,2,4,6,8,0]))

#결과를 보면 1 3 5 7 9 ~~이렇게 아무렇게나 막 넣었는데 return값은 정렬되서나온다

#이게 바로 우선 순위 큐의 개념 ==>가장 작은 정수의 값부터 나오게 된다(우선순위)
#파이썬의 우선순위 큐는 무조건 최소힙 ==>작은 수부터 나온다. Max heap을 하려면 부호를 반대로 해서 넣어준다(아래처럼)
# heapq.heappush(array,-value)  ==> -heapq.heappop(array) 이렇게 -로 넣어주고 뺄때 -붙여서 빼면 Max Heap이다.

#Tuple을 넣을때는 첫번째 원소의 값을 기준으로 우선순위가 결정된다.