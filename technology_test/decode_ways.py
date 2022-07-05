def decode_ways(s):

    dp = {len(s): 1}

    def dfs(i):

        # base cases
        if i in dp:
            return dp[i]
        if s[i] == "0":
            return 0
        
        # if not zero
        res = dfs(i+1)

        if (i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
            res += dfs(i+2)

            dp[i] = res
        
        return res
    
    return dfs(0)


print(decode_ways("226"))