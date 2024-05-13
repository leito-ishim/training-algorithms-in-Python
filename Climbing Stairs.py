# You are climbing a staircase. It takes n steps to reach the top.
#
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


def climbStairs(n):
    if n == 0 or n == 1:
        return 1
    return climbStairs(n - 1) + climbStairs(n - 2)


print(climbStairs(2))
print(climbStairs(4))
