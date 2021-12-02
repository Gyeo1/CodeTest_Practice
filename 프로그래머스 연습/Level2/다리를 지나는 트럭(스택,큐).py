from collections import deque
#문제 접근 방법==> 다리의 길이 만큼 deq 초기화 후 트럭을 deq에 append 시키고 무게 비교를 하면서 한칸씩 옆으로 밀어주는 큐
#다리의 길이는 항상 유지되도록 설계, max나 sum의 시간 복잡도가 O(N)이므로 Loop에서는 사용하지 말자.
def solution(bridge_length, weight, truck_weights):
    deq=deque([0]*(bridge_length))
    i=0
    answer=0
    deq.append(truck_weights[i])
    sum_value=sum(deq)              #미리 sum 값을 받아 놓고 값에서 +-를 시켜야 시간 복잡도가 줄어든다.
    while truck_weights[i] in deq:  #max(deq)에서 바꾼 부분. 항상 truck 무게의 최신값을 확인하는 방향으로!
        sum_value-=deq.popleft()
        answer += 1
        if i<len(truck_weights)-1 and sum_value+truck_weights[i+1]<=weight:#sum_value를 활용
            i+=1
            deq.append(truck_weights[i])
            sum_value+=truck_weights[i]     #sum_value 값 갱신
        if len(deq)<bridge_length:# 다리의 길이는 항상 유지 시켜준다.
            deq.append(0)
    return answer

# bridge_length=2 #최대 올라갈수 있는 트럭 수 == 다리 길이이다.
# weight=10     #다리가 견딜수 있는 무게
# truck_weights=[7,4,5,6] # 각 트럭의 무게

bridge_length=100 #최대 올라갈수 있는 트럭 수 == 다리 길이이다.
weight=10     #다리가 견딜수 있는 무게
truck_weights=[10] # 각 트럭의 무게
print(solution(bridge_length,weight,truck_weights))
#모든 트럭이 지나가려면 걸리는 시간을 구하기

#시간 복잡도의 중요성! max나 sum은 복잡도가 O(N)임. 매 loop마다 이를 반복하는 것은 매우 비효율적이다.
