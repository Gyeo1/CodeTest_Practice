#https://www.acmicpc.net/problem/1013   골드5

import re

#문제 접근 방법 1)일단 01패턴은 발견시 무조건 없앤다
#2)100+1+패턴을 발견이 맨 뒤에 100이나 01로 시작하지 않는다면 패턴을 계속이어간다
#WHY? ==>10001뒤에 1111이 올수도 있고 101010 이올수도 있고 00001이 올수도있음.
#하지만 100+1+뒤에 다시 100+1+|01 을 만족할 수 있는 패턴은 1이 연속으로 오거나 100으로 시작하거나 01로 끝나는것 뿐임

def find_pattern(s):
    start=0
    # print(s)
    for i in range(1, len(s) + 1):
        new_s = s[start:i] #처음부터 한칸씩 뒤로간다 010000이면 0 01 010 0100이런식
        check = re.findall(r'100+1+|01', new_s) #new_s에서 100+1+|01 패턴을 찾아 check에 할당

        if len(check)>1:#check에는 항상 패턴 1개만 들어감 ==> 패턴 완성시 다음 인덱스 부터 시작하므로
            print("NO")
            return False

        if new_s =='01':#==>01은 무조건 지워줌, 01은 100+1+과 어우러질수 없기 때문
            start=i
            continue

        if new_s in check: #new_s가 패턴에 겹치게 되면? s의 i인덱스 뒤를확인
            if i+2<len(s)+1 and s[i:i+2]=='01': #01 패턴 발견시 다음부터 시작
                start=i                         #100+1+과 01은 이어질 수 없기때문임
                continue
            if i+3<len(s)+1 and s[i:i+3] =='100': #새로운 100+ 패턴 발견시
                start=i                           #그러면 100+1+패턴을 찾으면 되니깐 다음부터 다시 시작
                continue
            #if 문 통과를 못했으면 2가지임 1)패턴이 안끝났다(100+1+에서 1이 계속 반복중)
            #2)패턴이 망가졌다 --> 뒤로가면 check에 2개의 패턴이 들어갈때 까지 반복

    #check에 값이 있고 new_s랑 패턴이 같으면 YES임, 그리고 check는 어짜피 1개다.
    if check and new_s==check[0]:
        print("YES")
        return
    print("NO")


number=int(input())
for _ in range(number):
    string=input()
    find_pattern(string)
