def climbStairs( n):
    """
    :type n: int
    :rtype: int
    """
    methods_num = [0] * (n+1)
    methods_num[0] = 1
    methods_num[1] = 1

    for i in range(2, n+1):
        methods_num[i] = methods_num[i-1] + methods_num[i-2]
    
    return methods_num[n]



n1 = 2
n2 = 3
print(climbStairs(2))
print(climbStairs(3))
