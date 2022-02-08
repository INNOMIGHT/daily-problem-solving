def best_time_calculator(prices):

    cur_max = 0
    max_val = 0
    if len(prices) > 0:
        cur_val = prices[0]
    
    for i in range(len(prices)):
        if cur_val > prices[i]:
            cur_val = prices[i]
        cur_max = max(prices[i] - cur_val, cur_max)
        if cur_max > max_val:
            max_val = cur_max
    
    return max_val