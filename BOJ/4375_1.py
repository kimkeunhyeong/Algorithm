from sys import stdin
from math import log10

data = [int(i) for i in stdin.readlines()]

for i in data:
    start = 1
    for _ in range(int(log10(i))):
        start = start * 10 + 1
    while True:
        if start % i:
            start = start * 10 + 1
        else:
            print(len(str(start)))
            break