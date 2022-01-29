#https://www.acmicpc.net/problem/2941 (실버 5 문제)

import sys ,re
# input=sys.stdin.readline

check=['c=','c-','dz=','d-','lj','nj','s=','z=']
a=input()
for i in check:
    if i in a: #크로아티아 문자열이 있는지 확인
        a=re.sub(i,'1',a) #re.sub 함수(패턴, 패턴을 어떻게 바꾸냐, 적용시킬 문자열)

        # print(a)
print(len(a))