#문제 ==> 카드를 오름차순으로 정렬하시오(선택정렬)
array=[0,5,9,7,3,1,6,2,4,8]
count=0
for i in range(len(array)):
    for j in range(i,len(array)): #단계가 올라갈수 록 반복 수는 작아짐
        if array[i]>array[j]:
            array[i], array[j]= array[j], array[i] #Swap 알고리즘! 파이썬의 특징이다.
            count +=1

print(array, count)