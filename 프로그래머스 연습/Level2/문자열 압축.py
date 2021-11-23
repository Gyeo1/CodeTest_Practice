from collections import deque
deq=deque()
def solution(s):
    answer = 0
    length=[]
    index=[]
    value=0
    max_index=0
    for j in range(len(s)):
        check=""
        for i in range(len(s)-j):
            if i + 1 < len(s) - 1 and s[i] == s[i + 1]:
                length.append(1)
            check += s[j+i]
            if check in s[i+j + 1:]:
                length.append(len(check))
                index.append(j)
        # if len(check)==1 and s[i]==s[i+1]:
    value=max(length)
    max_index=index[length.index(max(length))]
    if max_index!=0 and max_index%value==0:
        while 1:
            if s[max_index:max_index+value+1]==s[max_index+value+1:]:
                k=max_index+value+1


    elif max_index==0 and s[max_index:max_index+value+1]:




    print(length, len(length))
    print(index,len(index))
    print("최대 길이가 시작되는 인덱스는: ",index[length.index(max(length))])
    print(max(length))
    return answer


s="abcabcdede"
a=solution(s)

# # print(s[0])
# # for i in range(len(s)):
# #     a+=s[i]
# #     deq.append(a)
# # print(deq)
# # print(a)
# # if a==s:
# #     print("중복입니다")
# #문제 어떻게 짤라야지 최소 문자열로 압축 가능?
# #문자가 중복되기 시작하는 인덱스 찾고 앞의 인덱스/길이 값이 나눠 지면 된다.
