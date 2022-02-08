# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.


def twoSum(self, nums: List[int], target: int) -> List[int]:
    to_find = []
    
    for num in range(len(nums)):

        if nums[num] in to_find:
            return [num, to_find.index(nums[num])]
        else:
            to_find.append(target-nums[num])