
import copy
def dfs(idx,current,idx_list):
    global payment,min_list
    if current[4]>payment:
        return

    if current[0]>=need[0] and current[1]>=need[1] and current[2] >= need[2] and current[3]>=need[3]:
        if payment>current[4]:
            payment=current[4]
            min_list=copy.deepcopy(idx_list)
        return
    if idx>=N:
        return
    check=copy.deepcopy(current)
    idx_list.append(idx+1)
    for i in range(5):
        check[i]+=menu[idx][i]
    dfs(idx+1,check,idx_list)
    idx_list.pop()
    for j in range(5):
        check[j]-=menu[idx][j]
    dfs(idx+1,check,idx_list)

    return


N=int(input())
menu=[]
min_list=[]
need=list(map(int, input().split()))
for _ in range(N):
    a=list(map(int,input().split()))
    menu.append(a)
payment=10**6 #일단 큰값을 기준으로 잡는다print(need)

for i in range(N):
    list_1=menu[i]
    idx_list=[i+1]
    dfs(i+1,list_1,idx_list)
if payment==(10**6):
    print(-1)
else:
    print(payment)
    for i in min_list:
        print(i,end=" ")