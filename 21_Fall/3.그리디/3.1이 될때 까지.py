#N이 1이 될때까지 N-1을 하던가 N/K를 한다. 이때 N/K는 나눠질때만 한다.
import time
N,K=map(int, input().split())
start_time = time.time()# 측정 시간
count=0
if 2<=N<=1000000 and 2<=K<=100000 and K<=N:
    while N!=1:
        if N%K==0:
            N=N/K
            count+=1
        else:
            N-=1
            count+=1
    print(count)


end_time=time.time()# 측정 종료
print("걸린시간은 ?:", end_time-start_time);