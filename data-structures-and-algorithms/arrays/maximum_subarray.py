# Given an integer array nums, find the contiguous subarray (containing at least one number) 
# which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.

# Kadane's Algorithm

def maxSubArray(nums):
    cur_max, max_till_now = 0, -10**4
    for c in nums:
        cur_max = max(c, cur_max + c)
        max_till_now = max(max_till_now, cur_max)
    return max_till_now


print(maxSubArray([-1, -2]))
