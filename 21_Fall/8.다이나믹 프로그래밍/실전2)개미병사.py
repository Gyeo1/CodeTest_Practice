import random, time
N=int(input())
# K=list(map(int,input().split()))
K=[]

start=time.time()
for i in range(N):
    K.append(random.randint(0,1000))
print(K)
a=[]
store=[0]*101

for i in range(N-1):
    for j in range(2,N):
        if i+j>=N:
            break
        a.append(K[i]+K[i+j])
    if len(a)!=0:
        store[i]=(max(a))
    a.clear()
print(max(store))
print("걸린 시간:",time.time()-start)