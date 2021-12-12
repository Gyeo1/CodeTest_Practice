def solution(name):
    check=["A"] * len(name)
    value_list=[]
    length_list=[]
    #아래 for문 ==> 조이스틱이 위 아래로 움직이는 최소 값 구하는 for문
    for j in range(len(check)):
        value=ord(name[j])-ord(check[j])
        if value>13: #A-Z상 N이 중간 위치 가는데 걸리는 거리는 13이기 때문.
            # 무슨뜻? ==>A--> 타겟까지 가는것 보다 Z부터 세는게 더 빠르다는 의미
            value=ord("Z")-ord(name[j])+1
        value_list.append(value)
    print(value_list)

    #idx 기준 인덱스를 기반으로 뒤집어서 길이를 재는 함수
    #왜 사용 하냐면 결국 조이스틱이 뒤로 되돌아 가는 경우 최소값을 구하기 위해서
    def find_length(val_list,idx):
        val2=(val_list[:idx+1]+list(reversed(val_list[:idx]))+list(reversed(val_list[idx+1:])))
        while 1:
            if val2[-1]==0:             #0인 경우는 조이스틱이 안가도 되기 때문에 길이상에서 지워버린다.
                del val2[-1]
            else:
                break
        length_list.append(len(val2)-1)
        #-1하는 이유는 len은 전체길이 값인데 조이스틱은 idx=0기준은 움직임으로 포함 안시키기 때문이다

    #우선 조이스틱이 -> <-로 움직이는 최소 값을 구하기 전에 idx=0일때 기준으로 오른쪽으로 가는 경우를 구한다
    val1=value_list[:]
    while 1:
        if max(val1)==0:
            break
        elif val1[-1]==0:
            del val1[-1]
        else:
            break
        length_list.append(len(val1)-1)
    for k in range(len(value_list)-1):
        if max(val1)==0:
            length_list.append(0)
            break
        v_list=value_list[:]
        find_length(v_list,k)
    print(sum(value_list))
    print(length_list)
    answer=sum(value_list)+min(length_list)
    return answer


name="AAAAZ"

# print([0 * len(name[:5])])
print(solution(name))

# a=ord("O")-ord("A")
# if a<13:
#     value=a
# else:
#     value=ord("Z")-ord("O")+1
# print(value)

#조이스틱을 활용해 주어진 name을 만들려면 필요한 횟수를 return해라 처음엔 A만 주어진다.
#위, 아래, 오른쪽, 왼쪽이 있다
#위쪽: 다음 알파벳     아래쪽:이전 알파벳     오른쪽:커서를 으른쪽으로    왼쪽:커서를 왼쪽(처음 커서에있다면 맨 뒤로)