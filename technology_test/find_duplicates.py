def findDuplicates(self, nums):
        
        duplicates = set()
        length = len(nums)
        j = 0
        i=0
        if len(nums) > 0:
            while j < length:
                if nums[i] not in duplicates:
                    duplicates.add(nums[i])
                    nums.pop(i)
                else:
                    i+=1
                    j+=1
                length = len(nums)
            
            
                
        return nums