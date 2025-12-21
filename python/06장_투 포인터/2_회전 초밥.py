# https://www.acmicpc.net/problem/15961

import sys

n, d, k, c = map(int, sys.stdin.readline().split())
sushi = []
for _ in range(n):
    sushi.append(int(sys.stdin.readline()))

sushi = sushi + sushi[:k]

sliding_num = [0] * (d+1)
type_num = 0

for i in range(k):
    sushi_num = sushi[i]
    if sliding_num[sushi_num] == 0: type_num += 1
    sliding_num[sushi_num] += 1

# 보너스로 주는 초밥의 종류를 먹지 않았다면 먹은 초밥 종류에 1 추가
result = type_num + 1 if sliding_num[c] == 0 else 0

for i in range(k, len(sushi)):
    sushi_num = sushi[i]
    remove_num = sushi[i-k]

		# 이전에 없던 초밥 종류인 경우 종류 하나 추가
    if sliding_num[sushi_num] == 0:
        type_num +=1
    sliding_num[sushi_num] += 1

    # 특정 초밥 종류의 갯수를 하나 줄였는데 0이 된 경우 초밥 종류 하나 제거
    sliding_num[remove_num] -= 1
    if sliding_num[remove_num] == 0:
        type_num -= 1

    result = max(type_num + (1 if sliding_num[c] == 0 else 0), result)

print(result)