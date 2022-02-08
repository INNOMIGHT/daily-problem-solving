# Inputs - weight array, value array, W: max weight

def knapsack(weight_arr, val_arr, max_weight, n, total_val=0):
    dp = [[-1 for i in range(max_weight+1)] for j in range(n+1)]
    if n == 0 or max_weight==0:
        return total_val

    if dp[n][max_weight] != -1:
        return dp[n][max_weight]

    if weight_arr[n-1] > max_weight:
        dp[n][max_weight] = knapsack(weight_arr, val_arr, max_weight, n-1, total_val)
        return dp[n][max_weight]
    else:
        dp[n][max_weight] = max(knapsack(weight_arr, val_arr, max_weight-weight_arr[n-1], n-1, total_val = total_val+val_arr[n-1]), knapsack(weight_arr, val_arr, max_weight, n-1, total_val))
        return dp[n][max_weight]

print(knapsack([10, 20, 30], [60, 100, 120], 50, 3))