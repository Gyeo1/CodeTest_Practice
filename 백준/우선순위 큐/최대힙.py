import heapq,sys

list_1=[]
heap=[]
N=int(sys.stdin.readline())
for _ in range(N):
    list_1.append(int(sys.stdin.readline())) #이게 핵심이다! sys.stdin.readline()으로 받는게 속도가 더 빠르다
# print(list_1)
for i in list_1:
    if i !=0:
        heapq.heappush(heap,-i)
        #heapq는 원래 최소 힙만 지원해줌. 우선순위가 정수! 임을 생각해 -를 붙여주면 최대힙이 된다.
        continue
    if len(heap)!=0:
        print(-heapq.heappop(heap))
        continue
    print(0)

# print(heap)
