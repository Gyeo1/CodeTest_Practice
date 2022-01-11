import sys,heapq
input=sys.stdin.readline
INF=float('inf')
test_case=int(input())
def find_way(start,end):
    heap=[]
    dist=[INF]*(node+1)
    dist[start]=0
    heapq.heappush(heap,[0,start]) #무게, 시작 노드를 넣어준다.
    while heap:
        cost,check_node=heapq.heappop(heap)
        for n_node,n_cost in graph[check_node]:
            n_cost+=cost
            if dist[n_node]>n_cost:
                dist[n_node]=n_cost
                heapq.heappush(heap,[n_cost,n_node])
    if end ==0:
        return dist
    return dist[end]
for _ in range(test_case):
    node, lines, number= map(int,input().split()) #number는 목적지 후보 갯수이다.
    graph = [[] for _ in range(node + 1)] #양방향 도로
    #참고로 교차로 사이에는 도로가 많아도 한개!
    start_node,g,h=map(int,input().split()) #s는 예술가들의 출발지, g,h는 예술가들이 지나간 lines이다. g!=h임
    for _ in range(lines): #여기에 간선의 정보
        node1,node2, length=map(int,input().split())
        graph[node1].append([node2,length])
        graph[node2].append([node1,length])#양방향 간선 정보이니 둘다 넣어준다.
    destination=[]
    check1 = find_way(start_node, 0)  # 출발 지점 부터 모든 노드의 이동 배열을 받는다.

    for _ in range(number):#목적지 후보를 입력 , 목적지 후보는 모두 다른값이다. 100개 까지
        a=int(input())
        check2 = find_way(start_node, g) + find_way(g, h) + find_way(h,a) #g,h를 지나고 목적지로 가는 경우를 넣어서 둘이 비교해서 값이 같으면 출력
        check3= find_way(start_node, h) + find_way(h, g) + find_way(g,a)
        if check1[a]==min(check3,check2): #만약 g,h를 지나고 목적지로 가는 경우가 최단 경로이면
            destination.append(a)
        # print(check1,"목적지:",a,"구한 값:",min(check3,check2),", 최단경로: ",check1[a])
    for i in sorted(destination):
        print(i , end=" ")
    print("")
    #일단 최적의 경로로 가는 값을 구한다.
        # print(check1,check2)
#문제 느낌
#음 목적지로 갈때 최단의 경로+최소의 간선으로 갈 수 있는 경우를 선택해라 이건가? 일단 출발지에서 g,h까지의
