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