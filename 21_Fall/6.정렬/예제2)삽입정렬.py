#삽입 정렬 정리
# #내가 생각한 코드
# array=[0,5,9,7,3,1,6,2,4,8]
#
# for i in range(len(array)): #i가 현재 array의 인덱스
#         for j in range(i): #j는 i의 앞에있는 인덱스
#             if array[j]>array[i]:
#                 array[j],array[i]=array[i],array[j]
#
#
# print(array)

##정석 코드 ==> 왜 정석이냐? 뒤에서 앞으로 확인했어야 됨 왜냐면 이미 앞은 정렬된 상태라 가정했기 때문.

#만약 뒤에서 어중간하게 작은 값이 나오면 for문으로 반복하는 횟수가 쓸데 없이 많아진다!

array=[0,5,9,7,3,1,6,2,4,8]

for i in range(1,len(array)): #i가 현재 array의 인덱스
        for j in range(i,0,-1):
            if array[j]<array[j-1]: #앞쪽은 이미 정렬 된거라 가정 ==> 2개만 확인하면 된다.
                array[j],array[j-1]=array[j-1],array[j]
            else:
                break

print(array)