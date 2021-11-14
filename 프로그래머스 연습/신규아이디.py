import sys

def solution(new_id):

    #Step1 대문자 소문자로 바꿔주기
    for i in range(len(new_id)):
        a=ord(new_id[i])
        if a>=65 and a<=90:
            a+=32
            new_id[i]=chr(a)
    #Step2 알파벳 소문자 숫자 - _ . 제외하고 모두 제거
    for j in range(len(new_id)):
        a = ord(new_id[j])

    return str(new_id)

new_id=list(input())
if len(new_id)>=3 and len(new_id)<=15:
    print(solution(new_id))