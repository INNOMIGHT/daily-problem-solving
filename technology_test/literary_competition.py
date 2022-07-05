# knapsack
def literary_competition(n, t, points_arr, time_arr):

    # base_case
    if t == 0 or n == 0:
        return 0
    
    # choices
    if memo[t][n]!=  0:
        return memo[t][n]
    else:
        if t < time_arr[n-1]:
            memo[t][n]  = literary_competition(n-1, t, points_arr, time_arr)
            return memo[t][n]
        if time_arr[n-1] <= t:
            memo[t][n] = max(
                (points_arr[n-1] + literary_competition(n-1, t-time_arr[n-1], points_arr, time_arr)),
                (literary_competition(n-1, t, points_arr, time_arr))
                )
            return memo[t][n]
            
n = 3
t = 7
#initialise with appropriate value
memo = [[0 for i in range(t)]for j in range(n)]
print(literary_competition(3, 7, [2, 6, 9], [3, 5, 3]))

