array=[5,7,9,0,3,1,6,2,4,8]


def quick_sort(array):
    if len(array)<=1:
        return array
    pivot=array[0]
    tail=array[1:]

    #핵심, [x for x in tail if x>pivot]을 하면 tail에 있는 값을 하나씩 가져오는데 pivot보다 큰값을 넣는다.
    rigth=[x for x in tail if x>pivot]
    left=[x for x in tail if x<=pivot]

    return quick_sort(left)+[pivot]+quick_sort(rigth) #재귀 호출로 left와 rigth 사이드를 다시 quick sort시켜준다,
print(quick_sort(array))


l_side=[x for x in range(10) if x%2==0]

#정석 풀이
# array=[5,7,9,0,3,1,6,2,4,8]
#
# def quick(array,start, end):
#     if start>=end: #원소가 하나만 있는 경우?
#         return
#     #인덱스
#     pivot=start
#     left=start+1
#     rigth=end
#     while left<=rigth: #교차될때 까지?
#         while left<=end and array[left] <=array[pivot] :
#             left+=1 #인덱스를 계속 증가 시켜줌 언제까지? ==>pivot보다 작은 값이 나올때 까지.
#         while rigth>start and array[rigth] >=array[pivot]:
#             rigth-=1
#         if left>rigth:# 엇갈렸다면 피벗 교체
#             array[rigth], array[pivot] = array[pivot], array[rigth]
#         else:
#             array[left], array[rigth]=array[rigth], array[left]
#
#     #교차가 되면 재귀 함수로 다시 호출!.
#     quick(array,start, rigth-1)
#     quick(array, rigth+1, end)
# quick(array,0,len(array)-1)
# print(array)