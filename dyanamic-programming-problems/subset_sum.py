def subset_sum(arr, sum_t, n):

    dp = [[False for i in range(sum_t+1)] for j in range(len(arr)+1)]
    if sum_t == 0:
        return True
    elif n == 0:
        return False
    if arr[n-1] > sum_t:
        dp[n][sum_t] = subset_sum(arr, sum_t, n-1)
        return dp[n][sum_t]
    if arr[n-1] <= sum_t:
        dp[n][sum_t] = subset_sum(arr, sum_t-arr[n-1], n-1) or subset_sum(arr, sum_t, n-1)
        return dp[n][sum_t]


print(subset_sum([3, 34, 10, 4, 5, 2], 9, 6))