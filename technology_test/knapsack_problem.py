def knapsack_problem(W, weight_arr, val_arr, n, total_val=0):
    dp = [[-1 for i in range(W+1)] for j in range(n+1)]
    print(dp)

    if W == 0 or n == 0:
        return total_val
    
    if dp[n][W] != -1:
        return dp[n][W]

    if weight_arr[n-1] > W:
        dp[n][W] = knapsack_problem(W-weight_arr[n-1], weight_arr, val_arr, n-1, total_val=total_val + val_arr[n-1])
        return dp[n][W]
    else:
        dp[n][W] = max(knapsack_problem(W, weight_arr, val_arr, n-1, total_val), knapsack_problem(W-weight_arr[n-1], weight_arr, val_arr, n-1, total_val=total_val + val_arr[n-1]))
        return dp[n][W]


print(knapsack_problem(50, [10, 20, 30], [60, 100, 120], 3))