import time
#m번 더하기를 하는데 숫자는 k 번만 쓸수 있는 큰수의 법칙?
n,m,k=map(int,input().split())
data=list(map(int,input().split()))
result=0
count=0
start_time = time.time()# 측정 시간
if min(data)>=1 and max(data)<=10000 and len(data)==n and 2<=n<=1000 and 1<=m<=10000 and 1<=k<=10000 and k<=m:
    data.sort()
    biggest=data[n-1]
    second=data[n-2]
    for i in range(m):
        if count==k:
            result+=second
            count=0
        else:
            result += biggest
            count += 1


print(result)

end_time=time.time()# 측정 종료
print("걸린시간은 ?:", end_time-start_time);