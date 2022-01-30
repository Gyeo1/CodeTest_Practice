#K개의 글자만 읽을 수 있다 남극의 언어는 반드시 anta로 시작하고 tica로 끝난다 즉 a,t,n,i,c 5개의 문자는 반드시 알아야함
from itertools import combinations,product
essential=list(set("antatica"))
#접근 방법 ==>antatica의 알파벳을 주어진 str에서 제외하고 남은 알파벳수만큼 조합으로 만들고 확인한다?
#아래 for문은 주어진 string에서 a,n,c,i,t를 제외하고 남은 알파엣을 확인하는 것이다.
str_1=[]
N,K= map(int,input().split())
for i in range(N):
    ip=input()
    str_1.append(ip)
if K<5:#antatica의 5개의 알파벳은 필수이기 때문이다.
    print(0)
    exit()
elif K==26: #26이면 모든 알파벳을 품을 수 있기 때문에 모든 문자를 배울 수 있다.
    print(N)
    exit()

#a,n,t,i,c 의 5개의 문자를 다 빼준다.
for i in range(len(str_1)):
    str_1[i]=set(str_1[i])
    for j in essential:
        (str_1[i].discard(j))
    str_1[i]=list(str_1[i])

check_chr=""
for i in range(len(str_1)):
    for j in range(len(str_1[i])):
        if str_1[i][j] in check_chr:
            continue
        check_chr+=str_1[i][j]
print(str_1)
print(check_chr)
a=list(combinations(check_chr,K-5))
max_val=0
if len(a)<=K-5:
    #len(a)는 주어진 알파벳의 총 길이, K-5는 남은 배울수 있는 문자 수인데 K-5가 더 크면 모든 문자를 배울 수 있다.
    print(N)
    exit()
for i in range(len(a)):
    check_point=0
    for k in range(len(str_1)):
        count=0
        if len(str_1[k]) > K - 5:
            continue
        if len(str_1[k]) == 0:
            check_point += 1
            continue
        for j in range(len(a[i])):
            if a[i][j] in str_1[k]:
                count+=1
            if count==len(str_1[k]):
                break
        if count==len(str_1[k]):
            check_point+=1
    if check_point>max_val:
        max_val=check_point
print(max_val)
#a가 남은 알파벳의 조합을 순서대로 확인한다.



