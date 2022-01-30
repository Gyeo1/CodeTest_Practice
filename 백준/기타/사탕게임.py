given=[]
N=int(input())
for i in range(N):
    string=input()
    given.append(string)
trigger=0
result=0
#가로로 제일 긴 사탕을 찾는다.
def find_max1(a_list): #색이 반복되는 경우를 찾는다.
    max_val=1
    #양옆 확인
    for i in range(N):
        if max_val==len(a_list): #만약 max_val이 최대값(배열의 길이)이면 걍 break
            break
        count=1
        for j in range(N-1):
            if a_list[i][j]!=a_list[i][j+1]:
                if len(a_list[i][j+1:])<max_val:# 행렬의 남아있는 길이가 max_val보다 작으면 걍 나와라
                    break
                max_val=max(max_val,count)
                count=1
                continue
            count+=1
        max_val=max(count,max_val)
    #위아래 확인
    for k in range(N):
        count=1
        for l in range(N-1):
            if a_list[l][k]!=a_list[l+1][k]:
                max_val=max(max_val,count)
                count=1
                continue
            count+=1
        max_val=max(count,max_val)
    return max_val

#아래의 for문은 양옆을 바꾸는 경우
for i in range(len(given)):
    for j in range(len(given[i])-1):
        a = given[:]
        if a[i][j]!=a[i][j+1]:
            trigger=1
            a[i]=a[i][:j]+a[i][j+1:j+2]+a[i][j:j+1]+a[i][j+2:]
            result=max(find_max1(a),result)

# 아래는 위 아래로 바꾸는 경우
for i in range(len(given)):
    for j in range(len(given[i])-1):
        a = given[:]
        if a[j][i]!=a[j+1][i]:
            trigger=1
            chr1=a[j][i:i+1]
            a[j]=a[j][:i]+a[j+1][i:i+1]+a[j][i+1:]
            a[j+1]=a[j+1][:i]+chr1+a[j+1][i+1:]
            result=max(find_max1(a),result)

if trigger==1: #사탕의 위치를 바꿀경우(색이 다른게 있는 경우)
    print(result)
else:          #사탕의 위치를 안바꾼 경우(모두 같은색이므로 한줄N개만큼 먹으면된다)
    print(N)


#문제 풀이의 핵심 ==> 위아래 바꾸고 가로 세로 전체 확인하고, 양옆 바꾸고 가로 세로 전체 확인해 보면 된다.