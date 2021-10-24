#부품이 N개 있고 고유 번호가 있다. M개 종류의 부품을 대량으로 구매하겠다고 견적서를 요청.
#가게에 손님이 문의한 M개의 부품이 있는지 확인하는 프로그램 작성
import sys
N=int(sys.stdin.readline().strip())
store=list(map(int, sys.stdin.readline().split()))
store.sort()

M=int(sys.stdin.readline().strip())
request=list(map(int, sys.stdin.readline().split()))

def binary_search(store,target,start,end):
    if start>end: #싹다 뒤져봤을때 없으면 no를 리턴해준다.
        return "no"
    middle=(start+end)//2
    if store[middle]>target:
        end=middle-1
    if store[middle]<target:
        start=middle+1
    if store[middle]==target:
        return "yes"
    return binary_search(store,target,start,end)



for i in range(M):
    print(binary_search(store,request[i],0,len(store)-1),end=" ")