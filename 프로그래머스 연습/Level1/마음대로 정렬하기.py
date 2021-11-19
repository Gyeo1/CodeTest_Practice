def solution(strings, n):
    answer = []
    check=[]
    count=0
    answer = sorted(strings,key=lambda x:x[n])
    #n번째 인덱스가 일치하다면 ? => 사전형으로 정리 이게 핵심
    for i in range(len(answer)):
        if i+1<len(answer)and answer[i][n]==answer[i+1][n]: #인덱스 일치시
            count+=1
        else:
            check=answer[i-count:i+1]
            check.sort()
            answer[i-count:i+1]=check
            count=0
    return answer

strings=["abce", "abcd","abca" ,"cdx"]
n=2
print(solution(strings,n))
##sorted 두번으로 끝낼수 있었다..
# import operator
#
# def solution(strings, n):
#     answer = sorted(strings)
#     answer = sorted(answer, key=lambda x: x[n])
#     return answer