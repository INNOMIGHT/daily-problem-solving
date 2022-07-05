# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

class ClimbingStairs:

    def distinct_ways(self, n, cache={}):
        if n in cache:
            print("found", n)
            return cache[n]

        output = 0
        if n <=3 :
            output = n
        else:
            output += self.distinct_ways(n-1, cache) + self.distinct_ways(n-2, cache)
            cache[n] = output
        print(cache)
        return output

sol = ClimbingStairs()
print(sol.distinct_ways(10))