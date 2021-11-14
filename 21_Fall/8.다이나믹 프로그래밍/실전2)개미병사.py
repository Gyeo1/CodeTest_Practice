#문제 해석을 잘못함==> 나는 2개만 창고 터는줄 알았는데 아니였음 모든 창고를 털면서 안걸리게 하면서 max 값을 찾는게 정답이다.

import random, time
N=int(input())
K=list(map(int,input().split()))
# K=[]

start=time.time()
# for i in range(N):
#     K.append(random.randint(0,1000))
# print(K)
# a=[]
store=[0]*100
#
# for i in range(N-1):
#     for j in range(2,N):
#         if i+j>=N:
#             break
#         a.append(K[i]+K[i+j])
#     if len(a)!=0:
#         store[i]=(max(a))
#     a.clear()
# print(max(store))



# 다이나믹 프로그래밍(Dynamic Programming) 진행 (보텀업)
store[0] = K[0]
store[1] = max(K[0], K[1])
for i in range(2, N):
    store[i] = max(store[i - 1], store[i - 2] + K[i])

# 계산된 결과 출력
print(store[N - 1])
print("걸린 시간:",time.time()-start)