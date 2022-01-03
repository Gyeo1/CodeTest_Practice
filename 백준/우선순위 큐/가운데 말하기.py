#정수를 하나씩 외칠때 마다 말한 숫자의 중간값을 말한다. 이때 짝수면 두 수중에 작은 값을 말한다(캐스팅 활용)
#ex)1,5,2,10,-99,7,5를 외치면 1일때는 1밖에없으니 "1" , 5일때는 1,5 짝수이므로 작은값인 "1"
#2일때는 1 2 5이므로 "2", 10일때는 1 2 5 10중 2 5가 가운데 값이니 작은 값인 "2" 이런식으로 문제 풀이

#힙을 2개를 써서 왼쪽 힙에는 중간값 보다 작은 값, 오른쪽에는 큰값을 넣는다.
#중간값은 왼쪽 힙에 넣는다 왜? ==>짝수일때 작은 값을 넣음 즉 왼쪽의 Root가 중간값이여야 된다
#왼쪽 root가 무조건 중간값이다
import heapq,sys
N=int(input())
left_heap=[]
rigth_heap=[]
answer=[]
for _ in range(N):
    int_input=int(sys.stdin.readline())
    if len(left_heap)==len(rigth_heap):
        heapq.heappush(left_heap,-int_input)
        #왜? 왼쪽은 최대힙이 되야됨 즉 왼쪽의 [0]값은 항상 제일 큰값!
    else:
        heapq.heappush(rigth_heap,int_input)
    if rigth_heap and rigth_heap[0]<(-left_heap[0]):
        #만약 왼쪽 힙의 루트값이 오른쪽의 루트값보다 크다? ==> 그럼 안됨 left가 중앙값 기준으로 작은값이니까
        #따라서 왼쪽과 오른쪽의 루트값을 바꿔줘야된다.
        left_val=-(heapq.heappop(left_heap)) #왼쪽 루트는 최대힙이니깐 -값을 붙여서 설정
        rigth_val=heapq.heappop(rigth_heap)
        heapq.heappush(left_heap,-(rigth_val)) #마찬가지로 최대힙이니깐 -붙여준다.
        heapq.heappush(rigth_heap,left_val)
    answer.append(-left_heap[0])

for i in answer:
    print(i)