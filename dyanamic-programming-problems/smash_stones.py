def smash_stones(stones):

    stones.sort()
    flag = 0
    i = 1
    length = len(stones)
    while flag != 1:
        new_stones = []
        new_stones.sort()
        diff = stones[i] - stones[i-1]
        print(stones[i], stones[i-1])
        if diff != 0:
            new_stones.append(diff)
        if i + 2 > length:
            length = len(new_stones)
            i=0
        i += 2
        if len(new_stones) == 1:
            flag = 1
    
    return new_stones
        



print(smash_stones([2,7,4,1,8,1]))