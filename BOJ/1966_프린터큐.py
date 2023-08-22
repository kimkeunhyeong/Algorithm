from sys import stdin
from collections import deque
input = stdin.readline

n = int(input())
for _ in range(n):
    doc_cnt, target_doc = map(int, input().split())
    documents = deque((index, value) for index, value in enumerate(map(int, input().split())))
    
    cnt = 0
    while documents:
        if len(list(filter(lambda x : x[1] > documents[0][1], documents))):
            documents.append(documents.popleft())
        else:
            cnt += 1
            if documents.popleft()[0] == target_doc:
                print(cnt)