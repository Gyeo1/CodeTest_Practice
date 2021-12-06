import math
def solution(expression):
    expression = list(expression)
    find_exp= [i for i in ("-", "+", "*") if i in expression]
    check=[]
    def calculation(priority,exp):
        print(priority, exp)
        index=0
        while priority not in exp:
            str_left=""
            str_rigth=""
            count_left=0
            count_rigth=0
            if priority[index] not in exp: #우선순위의 수식이 없다면 다음 우선순위로 넘겨준다.
                index+=1
                if index>=len(priority):
                    break
            priority_index=exp.index(priority[index])       #우선순위의 수식이 있는 인덱스 반환
            print(priority_index)
            for i in range(1,4):#피 연산자는 최대999임, 해당 for문은 index 기준 오른쪽 숫자 파악용임
                if priority_index+i<len(exp) and exp[priority_index+i] not in priority:
                    #맨처음 단계에선 50이 5, 0 이렇게 len=1로 분리됨
                    # if len(exp[priority_index+i])==1:
                    str_rigth+=exp[priority_index+i]
                    count_rigth+=1
                    continue
                if len(exp[priority_index+1])>1:
                    count_rigth=1
                break
            #아래는 왼쪽 확인
            for j in range(1,len(exp)):
                if priority_index-j>=0 and exp[priority_index-j]not in priority:
                    count_left+=1
                    continue
                # if len(exp[priority_index-j])>1:
                #     count_left=1
                break
            for k in range(count_left,0,-1):
                str_left+=exp[priority_index-k]
            print(str_left, str_rigth)
            #구해진 숫자들로 수식 계산
            if priority[index]=="*":
                check_middle=[str(int(str_left)*int(str_rigth))]
            elif priority[index]=="+":
                check_middle = [str(int(str_left) + int(str_rigth))]
            else:
                check_middle = [str(int(str_left) - int(str_rigth))]

            check_left=exp[:priority_index-count_left]
            check_rigth=exp[priority_index+count_rigth+1:]
            exp=check_left+check_middle+check_rigth
            print(exp)
        return exp
    if len(find_exp)>=2:
        for i in range(math.factorial(len(find_exp))//2):#우선순위 바꿔주기
            find_exp[len(find_exp)-1],find_exp[len(find_exp)-2]=find_exp[len(find_exp)-2], find_exp[len(find_exp)-1]
            # print(find_exp)
            #얕은 복사로 값을 넘겨준다.
            shallow_priority=find_exp[:]
            shallow_exp=expression[:]
            check+=(calculation(shallow_priority, shallow_exp))
            find_exp[0],find_exp[1]=find_exp[1],find_exp[0]
            #얕은복사
            shallow_priority = find_exp[:]
            shallow_exp = expression[:]
            check+=(calculation(shallow_priority, shallow_exp))
            # print(find_exp)
    else:   #연산자가 하나 뿐일때
        shallow_priority = find_exp[:]
        shallow_exp = expression[:]
        check += (calculation(shallow_priority, shallow_exp))
    check=[abs(int(n)) for n in check ]
    answer=max(check)
    return answer

expression="100+200+100+200"
print(solution(expression))
'''
#정규 표현식과 split을 활용해 코드를 아래처럼 매우 단축 시킬 수 있다!

import re #re는 정규 표현식을 쓴다는 의미
from itertools import permutations
expression="50*6-3*2"
n_epx=[n for n in ("-","*","+") if n in expression]
check=[]
expression = re.split(r'(\D)',expression) #r'(\D)는 정규 표현식으로 숫자가 아닌것을 기준으로 split한다는 의미

def calulate(express, priority):
    index=0
    while index<len(priority):
        priority_index=express.index(priority[index])

        if priority[index]=="*":
            middle=[int(express[priority_index+-1])*int(express[priority_index+1])]
        elif priority[index]=="+":
            middle = [int(express[priority_index -1]) + int(express[priority_index + 1])]
        else:
            middle = [int(express[priority_index -1]) - int(express[priority_index +1])]
        express=express[:priority_index-1]+middle+express[priority_index+2:]
        if priority[index] not in express:
            index+=1
    return express
for i in list(permutations(n_epx)):#순열로 우선순위 저장
    ex=expression[:]
    check+=calulate(ex,i)
check=[abs(int(v)) for v in check]
answer=max(check)
print(check,answer)

'''