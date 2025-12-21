# https://www.acmicpc.net/problem/1753

import heapq
import sys

input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
adj = [[] for _ in range(v+1)]
cost = [[] for _ in range(v+1)]

for _ in range(e):
    a, b, w = map(int,input().split())
    adj[a].append(b)
    cost[a].append(w)

#INF의 값을 바꿔서 제출해 보실수 있습니다.
INF = 0x3f3f3f3f

dist = [INF] * (v+1)
hq = [(0, k)]
dist[k] = 0

while hq:
    nowCost, now = heapq.heappop(hq)

    if nowCost > dist[now]:
        continue

    for next, nextCost in zip(adj[now], cost[now]):
        if dist[next] > nowCost + nextCost:
            dist[next] = nowCost + nextCost
            heapq.heappush(hq, (dist[next], next))

for d in dist[1:]:
    if d == INF:
        print('INF')
    else:
        print(d)