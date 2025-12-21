# https://www.acmicpc.net/problem/1931

import heapq

class meeting:
    def __init__(self,info):
        self.st, self.ed = info
    def __lt__(self, other):
        if self.ed != other.ed:
            return self.ed < other.ed
        return self.st < other.st

n = int(input())
info = []

for i in range(n):
    info.append(meeting(list(map(int,input().split()))))

heapq.heapify(info)
last = -1
res = 0

while info:
    m = heapq.heappop(info)
    st, ed = m.st, m.ed
    # 이전에 회의가 끝난 시간이 현재 회의 시작 시간 이상이어야함
    if last <= st:
        res += 1
        # 끝난 시간 갱신
        last = ed
print(res)