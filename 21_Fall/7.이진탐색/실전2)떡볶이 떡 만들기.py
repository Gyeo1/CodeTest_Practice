#떡을 자르는 절단기의 높이 H, 잘린만큼만 손님이 떡을 가져간다
#손님이 요청한 길이가 M일때 적어도! M만큼의 떡을 얻기 위해 설정할 수 있는 높이의 최대값?
import sys
N,M= map(int,input().split())
rice_cake=list(map(int,sys.stdin.readline().rstrip().split()))

def binary_search(array,start, end, target):
    middle=(start+end)//2                   #중간지점 인덱스
    middle_value=array[middle]              #중간 지점의 값 (==> 절단기 높이이다)

    while 1:
        sum = 0  # 항상 0 초기화

        if middle<start or middle>end:         #인덱스가 범위를 벗어 나면 오류
            return 0

        if array[middle-1]>=middle_value:       #칼날의 높이가 배열의 중간-1값과 같아 지거나 작아지면 다음 떡을 가리켜야된다.
            middle-=1
        elif array[middle+1]<=middle_value:
            middle+=1


        for i in range(middle,end+1,1):
            if(array[i]-middle_value)>=0:
                sum+=(array[i]-middle_value)         #떡 길이-기준점 높이의 떡길이

        if sum<target:                      #정해진 높이에서 떡을 잘랐을때의 합이 목표치보다 작다?
            middle_value-=1                 #높이를 내린다.
        if sum>target:
            middle_value+=1                 #높이를 올리고 다시 반복 why?==>최대값을 찾아야 되기 때문에
        if sum==target:
            return middle_value

if len(rice_cake)==N:
    rice_cake.sort()
    print(binary_search(rice_cake,0,len(rice_cake)-1,M))