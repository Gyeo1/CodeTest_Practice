#앵무새 꼬꼬
import sys
input=sys.stdin.readline
N=int(input())
check=['a','A','e','E','i','I','o','O','u','U']

def find_index(needed,string):
    start=0
    while 1:
        next_index=string.find(needed,start)
        if next_index ==-1:
            break
        index_list.append(next_index)
        start=next_index+1

for _ in range(N):
    string=input()
    index_list = []
    # print(string)
    for i in check: #찾으려는 모음을 가져온다.
        find_index(i,string)
    if len(index_list)==0:
        print("???")
        continue
    index_list.sort()
    for i in index_list:
        print(string[i],end="")
    print()