inputt = open('input4.txt', 'r')
output = open('output4.txt', 'w')

fline = inputt.readline().strip().split(" ")
N, X = int(fline[0]), int(fline[1])
coins = list(map(int, inputt.readline().strip().split(" ")))


def minCoins(N, X, coins):
    dp = [float('inf')] * (X + 1)
    dp[0] = 0

    for i in range(1, X + 1):
        for j in range(N):
            if coins[j] <= i:
                dp[i] = min(dp[i], dp[i - coins[j]] + 1)

    if dp[X] == float('inf'):
        return -1
    else:
        return dp[X]


output.write(minCoins(N, X, coins))
output.close()


# The `minCoins` function utilizes dynamic programming to find the minimum number of coins required to make up a target value (X) using the available coin denominations. It initializes an array `dp` where `dp[i]` represents the minimum number of coins needed to achieve value `i`. It iterates through each value from 1 to X, considering all available coin denominations and updating the minimum number of coins needed for each value. Finally, it returns the minimum number of coins required to achieve the target value X. If it's not possible to achieve X with the given coins, it returns -1.