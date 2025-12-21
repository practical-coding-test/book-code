# https://www.acmicpc.net/problem/2579

import sys
sys.setrecursionlimit(1000)

n = int(input())
stair = []

for num in range(n):
    stair.append(int(input()))

# 1. Top Down
cache = [[-1]*n for _ in range(3)]

def score_memoization(n, step):
    if n < 0: return 0
    if cache[step][n] != -1: return cache[step][n]
    cache[step][n] = stair[n] + max(score_memoization(n-1, 1) if step == 2 else -0x3f3f3f3f, score_memoization(n-2, 2))
    return cache[step][n]

print(score_memoization(n-1, 2))