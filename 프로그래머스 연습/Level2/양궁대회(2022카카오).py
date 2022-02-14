#https://programmers.co.kr/learn/courses/30/lessons/92342  2022카카오 블라인드

#k점을 더 많이 맞춘 사람이 해당 점수를 가져간다. 대신 동일 횟수로 맞추면 어피치에게 점수를 주는 패널티!
#추가 패널티는 점수가 같아도 어피치가 우승
max_val=0
answer=[]
def check_win(l1,l2):
    global max_val,answer
    #l1은 어피치 l2는 라이언 점수 값임
    apeach=0
    lion=0
    for i in range(len(l1)):
        if l1[i]<l2[i]:

            lion+=(10-i)
        elif l1[i]>l2[i]:
            apeach+=(10-i)
    print(l1, l2)
    print(apeach, lion)
    # if max_val<lion-apeach: #최대 점수차 갱신?
    #     answer=l2
    #     print(answer)
    #     max_val=lion-apeach

    if apeach<lion:
        return True
    return False

def solution(n, info):
    if n ==1 and info[0]==1:
        return [-1]
    for i in range(len(info)):
        check=[0 for _ in range(len(info))]
        for j in range(i,len(info)):
            if sum(check)+info[j]+1<=n:     #현재 lion이 쏜 횟수 + 어피치를 이기기 위해 쏜 횟수가 n보다 작으면 부여
                check[j]=info[j]+1
            # print(check)
            # if sum(check)>=n or :
            # if check_win(info,check): #이게 True면? 라이언 점수가 더 큼 그럼 j 기준 다음의 값으로 확인
            #     print(check)
            while check_win(info,check):
                check[j]=0
                j+=1
                if sum(check) + info[j] + 1 <= n:  # 현재 lion이 쏜 횟수 + 어피치를 이기기 위해 쏜 횟수가 n보다 작으면 부여
                    check[j] = info[j] + 1



n=9
info=[0,0,1,2,0,1,1,1,1,1,1]#10점부터 0점까지 맞춘횟수임.
solution(n,info)

print(max_val)

#n은 화살의 갯수
#info는 어피치가 맞춘 과녁의 점수임


#가장 큰 점수를 먹는 것 부터 쭉 내려온다?
