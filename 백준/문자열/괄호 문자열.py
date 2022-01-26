#https://www.acmicpc.net/problem/9012 백준 9012번
test_case=int(input())
def Is_VPS(value):
    check = value.count("(")
    # print(check)
    if len(value)%2!=0: #일단 ()가 한 쌍이여야되므로 2로 나눠져야 함
        print("NO")
        return
    if check != int(len(value)/2) or value[0]==')':
        #만약 (의 수가 딱 절반이 안되도 No임, 그리고 시작이)여도 안됨
        print("NO")
        return
    count=0
    for i in value:
        if count<0:#만약 밸런스가 깨짐 즉 ())이렇게 되면 그냥 탈출
            print("NO")
            return
        if i=='(':
            count+=1
        else:
            count-=1
    #문자열 한번 싹 훑고 나왔을때 count=0즉 (랑 )의 비율이 맞으면 YES임
    if count==0:
        print("YES")
    else:
        print("NO")
def IS_VPS_Advanced(value): #()가 매칭이되는 순간 pop을 시키는 개념
    check = value.count("(")
    list1=[]
    if len(value) % 2 != 0:  # 일단 ()가 한 쌍이여야되므로 2로 나눠져야 함
        print("NO")
        return
    if check != int(len(value) / 2) or value[0] == ')':
        # 만약 (의 수가 딱 절반이 안되도 No임, 그리고 시작이)여도 안됨
        print("NO")
        return
    for i in value:
        if i=="(":
            list1.append(i)
        else:
            if len(list1)!=0 and list1[-1]=="(": #만약 )인데 바로 아
                list1.pop()

    if len(list1)==0:
        print("YES")
    else:
        print("NO")


for _ in range(test_case):
    string=input()
    # Is_VPS(string)
    IS_VPS_Advanced(string)