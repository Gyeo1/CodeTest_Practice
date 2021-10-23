#계수 정렬은 특정 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘
array=[7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]
check=[]

# for i in range(len(array)):
#     check[array[i]]+=1 #각 데이터의 인덱스를 +1 시켜준다.

for i in range(len(array)):
    for j in range(len(array)):
        if i == array[j]:
            check.append(i)
print(check)

''' 정렬 라이브러리를 사용한 방법이다. 
result=sorted(array)
print(result)
array.sort()
print(array)
'''