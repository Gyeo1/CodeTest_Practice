#카드 게임: 행을 고르고 행에서 가장 작은 숫자중 제일 큰수를 가진 행을 찾는것?
import time
card=[]
mini=[]
n,m=map(int,input().split())
for i in range(n):
    data=list(map(int,input().split()))
    if len(data)==m:
        card.append(data)
    else:
        card.clear()
        break
start_time = time.time()# 측정 시간

if len(card)==n:
    for i in range(n):
        mini.append(min(card[i]))
    print(max(mini))

end_time=time.time()# 측정 종료
print("걸린시간은 ?:", end_time-start_time);