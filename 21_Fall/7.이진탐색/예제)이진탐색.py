#이진 탐색? ==>시작,끝, 중간점에서 중간점 기준으로 반씩 짤라서 탐색을 하는 개념이다
#반드시 정렬된 array를 가져야 된다.

array=list(map(int,input().split()))
array.sort()
target=int(input())
def binary_search(array,start,end,target):
    if start>end:
        return None
    middle=(start+end)//2 #몫만 가져옴 == 중간값
    if array[middle]>target: #중간 값이 타겟값 보다 크다? 끝점을 중간값으로!
        end=middle-1
    if array[middle]<target: #중간 값이 타겟 값 보다 작다? target은 middle 뒤에 있다.
        start=middle+1
    if array[middle]==target:
        return middle
    return binary_search(array,start,end,target) #재귀함수!


print(binary_search(array,0,len(array)-1,target))