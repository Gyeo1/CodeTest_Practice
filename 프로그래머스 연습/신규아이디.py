import sys

def solution(new_id):

    for i in range(len(new_id)):
        a=ord(new_id[i])
        if a>=65 and a<=90: #대문자 ?
            a+=32
            new_id[i]=chr(a)

    return str(new_id)

new_id=list(input())
if len(new_id)>=3 and len(new_id)<=15:
    print(solution(new_id))