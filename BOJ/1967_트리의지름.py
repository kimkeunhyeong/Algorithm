from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

def DFS(node, parent_weight):
    # 1. DFS로 root부터 최장길이를 탐색
    # -> DFS의 return값은 root로부터의 최대 길이, 마지막 노드 번호를 return하도록.
    # 2. 최장길이를 가지는 마지막 노드부터 DFS를 다시 실행하여 최장거리를 찾는다.
    accum_length = parent_weight
    last_node = node
    Visited[node] = True

    weights = []
    for next_node, weight in Tree[node]:
        if not Visited[next_node]:
            weights.append(DFS(next_node, weight))
    if weights:
        length, last_node = max(weights)
        accum_length += length

    return (accum_length, last_node)

input = stdin.readline

node_cnt = int(input())
Tree = [[] for i in range(node_cnt + 1)]
for i in range(node_cnt - 1):
    parent, child, weight = map(int, input().split())
    Tree[parent].append([child, weight])
    Tree[child].append([parent, weight])

Visited = [False] * (node_cnt + 1)
target_node = DFS(1, 0)[1]

Visited = [False] * (node_cnt + 1)
print(DFS(target_node, 0)[0])