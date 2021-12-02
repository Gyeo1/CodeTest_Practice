
def solution(clothes):
    dic=dict()
    check = []
    answer=1
    for i,j in clothes:         #이 for문에서 Type과 cloth를 재 정렬해준다.
        if dic.get(j)==None:
            dic[j]=[""]         #안입었을 경우 추가 행렬 type으로 추가해서 append시 같이 묶이게 한다.
            dic[j].append(i)    #첫번째 옷 추가
            continue
        dic[j].append(i)        #나머지 옷들은 append로 추가.
    print(dic)
    for k in dic:
        answer*=len(dic[k])     #수식의 이해= 옷입는 경우의 수 이다.
    # for i in dic.keys():
    #     check.append(dic[i])
    # # print(list(set(combinations(*check))))
    # answer=len(list(set(product(*check))))-1        #아무것도 안입는 경우를 -1해준다.
    return answer-1
clothes=[["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))
