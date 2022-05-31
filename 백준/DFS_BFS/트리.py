# https://www.acmicpc.net/problem/1068 골드 5

# 리프노드 => 자식의 개수가 0인 노드임
# 노드 하나를 지우면 해당 노드부터 자식까지 다 지워짐
from collections import deque


def solution(node, remove_node):
    root_node = node.index(-1)  # 루트 노드 찾아 놓기
    answer = 0
    if remove_node == root_node:
        print(answer)
        return
    check = [[] for _ in range(N)]
    rem_list = deque()
    rem_list.append(remove_node)
    node[remove_node] = -2

    while rem_list:  # 지우는 노드와 자식 노드들을 -2로 바꿔준다.
        val = rem_list.popleft()
        while val in node:
            idx = node.index(val)
            rem_list.append(idx)
            node[idx] = -2
    # print(node)
    for i in range(len(node)):  # 남은 노드끼리 연결 정보를 check에 저장
        if node[i] == -2 or i == root_node: # -2는 지워진 노드, root 노드는 -1이므로 pass 함
            continue
        check[i].append(node[i])
        check[node[i]].append(i)
    # print(check)
    if check[root_node] == []:  # 루트 노드에 연결된 자식이 없다면 자기 자신만 남았으므로 리프 노드는 1
        print(1)
        return

    for i in range(len(node)):
        if i == root_node:  # 루트 노드는 스킵
            continue
        if len(check[i]) == 1:  # check=1이면 부모밖에 연결된 사람이 x 즉 리프 노드(자식이 없는)이다.
            answer += 1
    print(answer)


N = int(input())
node = list(map(int, input().split()))  # -1이 root 노드, 나머지는 연결된 노드를 뜻함
remove_node = int(input())
# print(node)
solution(node, remove_node)
