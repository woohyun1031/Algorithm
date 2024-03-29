# 이친수는 0으로 시작하지 않는다.
# 이친수에서는 1이 두 번 연속으로 나타나지 않는다. 즉, 11을 부분 문자열로 갖지 않는다.
# 예를 들면 1, 10, 100, 101, 1000, 1001 등이 이친수가 된다. 하지만 0010101이나 101101은 각각 1, 2번 규칙에 위배되므로 이친수가 아니다.

# N(1 ≤ N ≤ 90)이 주어졌을 때, N자리 이친수의 개수를 구하는 프로그램을 작성하시오.

n = int(input())
dp = [[] for _ in range(n + 1)]
dp[0] = 0
dp[1] = 1

for i in range(2, n + 1):
    dp[i] = dp[i-1] + dp[i - 2]

print(dp[n])
