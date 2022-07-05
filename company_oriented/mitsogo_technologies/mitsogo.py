N = int(input())
arr = map(int,input().split())
cost = map(int,input().split())


def computeCost(arr, N, X,cost):
 
    cost = 0
    for i in range(N):
        cost += (abs(arr[i] - X)*cost[i])
    return cost

def minCostToMakeElementEqual(arr, N,cost):
 
    low = high
    high = arr[0]
    for i in range(N):
     
        if (low > arr[i]): low = arr[i]
        if (high < arr[i]): high = arr[i]

    while ((high - low) > 2):
     
        
        mid1 = low + (high - low) // 3
        mid2 = high - (high - low) // 3
 
        cost1 = computeCost(arr, N, mid1,cost)
        cost2 = computeCost(arr, N, mid2,cost)
 
        
        if (cost1 < cost2):
            high = mid2
 
       
        else:
            low = mid1
     

    return computeCost(arr, N, (low + high) // 2,cost)
 
# Driver code
print(minCostToMakeElementEqual(arr, N,cost))

