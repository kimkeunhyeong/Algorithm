from heapq import *
from collections import defaultdict
from sys import stdin

input = stdin.readline

TC = int(input())

for _ in range(TC):
    N = int(input())
    min_Q = []
    max_Q = []
    num_stat = defaultdict(int)
    IOCnt = 0 # In/Out count

    for __ in range(N):
        oper, num = input().split()
        if oper == "D":
            if IOCnt > 0: # 큐에 값이 존재하는 경우
                if num == "1":
                    while max_Q and num_stat[deleted := -heappop(max_Q)] == 0: # 삭제되지 않은 값이 나올때까지 pop
                        pass
                else:
                    while min_Q and num_stat[deleted := heappop(min_Q)] == 0:
                        pass
                num_stat[deleted] -= 1
                IOCnt -= 1

        else:
            # num을 input시에만 형변환하도록 수정하니 시간이 824ms(14%) 줄어듦.
            num = int(num)
            num_stat[num] += 1
            IOCnt += 1
            heappush(min_Q, num)
            heappush(max_Q, -num)

    if IOCnt > 0:
        # 큐에 값이 존재하고, 한 방향으로만 pop이 된 경우가 있을 수 있으므로 삭제된 값을 확인해야 함.
        while max_Q and num_stat[max_value := -heappop(max_Q)] == 0:
            pass
        while min_Q and num_stat[min_value := heappop(min_Q)] == 0:
            pass

        print(max_value, min_value)
    else:
        print("EMPTY")