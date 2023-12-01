from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)

def DFS(node, parent_weight):
    # reuse DFS code from prob no. 1967
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

for i in range(node_cnt):
    data = list(map(int, input().split()))
    node = data[0]
    for index in range(len(data) // 2 - 1):
        connected, distance = data[index * 2 + 1], data[(index + 1) * 2]
        Tree[node].append((connected, distance))

Visited = [False] * (node_cnt + 1)
target_node = DFS(1, 0)[1]

Visited = [False] * (node_cnt + 1)
print(DFS(target_node, 0)[0])