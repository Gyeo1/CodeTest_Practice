#https://www.acmicpc.net/problem/1013   골드5

import re
def find_pattern(s):
    start=0
    # print(s)
    for i in range(1, len(s) + 1):
        new_s = s[start:i] #처음부터 한칸씩 뒤로간다
        check = re.findall(r'100+1+|01', new_s)#

        if len(check)>1:
            print("NO")
            return False
        if new_s =='01':
            start=i
            continue
        if new_s in check: #new_s가 패턴에 겹치게 되면? 뒤에 2개를 확인 10001일때 10이나 01이면 끊기
            if i+2<len(s)+1 and s[i:i+2]=='01': #01 패턴 발견시
                start=i
                continue
            if i+3<len(s)+1 and s[i:i+3] =='100': #새로운 100+ 패턴 발견시
                start=i
                continue
    # print('결과로 나오는것: ', new_s,check)
    if check and new_s==check[0]:
        print("YES")
        return
    print("NO")
    # for i in range(1,len(s)+1):
    #     new_s=s[start:i]
    #     print(new_s)
    #     check=re.findall(r'100+1+|01',new_s)
    #     print(check)
    #     if '1001' in check or new_s=='01':
    #         if i+2<len(s) and s[i+1]=='1':
    #             continue
    #         start=i
    #         len_s+=len(check)
    # print("남은거?: ",check,new_s)
    # if (''.join(check)) == new_s:
    #     print("YES!")
    # else:
    #     print("No!")


number=int(input())
for _ in range(number):
    string=input()
    find_pattern(string)
# string='0110001010001'
# #
# string3='0110000111011000011101100001110110000111011000011101100001110110000111011000011101100001110110000111011000011101100001110110000111011000011101100001110110000111011000011101100001001100001110110000111'
# find_pattern(string3)


#시작 부터 끝~까지 인덱스 증가 시키면서 패턴 검색? 패턴 검색이 끝나면
#01일때는 무조건 지워야됨, 겹치는게 업기 떄문임.100+1+ 패턴은 계속 봐야됨 100+1+ 패턴일때는 지우지말고 뒤로가
#01은 무조건 지워