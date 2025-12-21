# https://www.acmicpc.net/problem/2003

n, m = map(int, input().split())
nums = list(map(int, input().split()))

s = 0
e = 0
sum = 0
result = 0

# e가 끝까지 왔을 경우 
while e < len(nums) or s < e:
    if e == len(nums):
        sum -= nums[s]
        s += 1
    else:
        if sum < m:
            sum += nums[e]
            e += 1
        else:
            sum -= nums[s]
            s += 1

    if sum == m:
        result += 1

print(result)