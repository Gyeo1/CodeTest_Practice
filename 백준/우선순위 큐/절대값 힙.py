import heapq,sys

N=int(input())
heap=[]
l_1=[]
for _ in range(N):
    l_1.append(int(sys.stdin.readline()))
for i in l_1:
    if i!=0:
        heapq.heappush(heap,(abs(i),i))
        continue
    if len(heap)!=0:
        print(heapq.heappop(heap)[1])
        continue
    print(0)