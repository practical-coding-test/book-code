# https://www.acmicpc.net/problem/11657

n, m = map(int, input().split())
INF = 500 * 6000 * 10000

edges = []
arrive_time = [INF] * (n + 1)
arrive_time[1] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

infinity_time_travel = False

for count in range(n):
    for a, b, time in edges:
        if arrive_time[a] == INF: continue
        if arrive_time[a] + time < arrive_time[b]:
            if count == n - 1:
                infinity_time_travel = True

            arrive_time[b] = arrive_time[a] + time
            
if infinity_time_travel:
    print(-1)
else:
    for city in range(2, n+1):
        if arrive_time[city] == INF:
            print(-1)
        else:
            print(arrive_time[city])