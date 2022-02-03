#https://www.acmicpc.net/problem/5430 골드 5문제

#AC는 정수배열의 연산을 위함, 2개의 함수 R(뒤집기) D(맨앞 삭제) 배열이 비었는데 D쓰면 에러

import re
from collections import deque


test_case=int(input())
def AC(order,check_list):
    flag=1 #flag가 1이면 정상, 0이면 뒤집힌 상태
    for i in order:
        if i=='D':
            if check_list: #리스트에 내용이 있다면
                if flag==1:#flag=1이면 맨 앞 삭제
                    check_list.popleft()
                else:#0이면 맨 뒤 삭제
                    check_list.pop()
            else:#리스트가 비어 있는데 d면 에러
                print("error")
                return False



        elif i=='R': #reverse 명령
            #만약 reverse함수를 쓰면 RRRRR일시 시간 초과가 발생한다
            #어짜피 D명령시 '1개'만 지운다.
            #flag로 1,0을 설정해 준다. 1일땐 맨 앞에(popleft)를 삭제, 0일땐 뒤를(pop)삭제하도록함
            if flag==1:
                flag=0
            else:
                flag=1

    if flag==0:#Flag=0인 상태로 끝나면 리스트를 뒤집고 RETURN한다.
        check_list.reverse()

    return check_list

for _ in range(test_case):
    request=input() #함수 순서를 받는다.
    deq1=deque()
    n=int(input())
    list_1=input()
    deq1.extend(re.findall(r'[\d]+',list_1)) #숫자만 빼서 deque에 넣어준다
    check=AC(request, deq1)
    if check != False:#error가 아닐시 문자열 출력
        print("["+",".join(check)+"]") #,를 기준으로 check의 값들을 붙여준다.

