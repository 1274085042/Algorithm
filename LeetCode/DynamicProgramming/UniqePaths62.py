import numpy as np
def uniquePaths(m, n):
    """
    :type m: int
    :type n: int
    :rtype: int
    """
    unique_paths = np.zeros((m, n), dtype=int)
    for j in range(n):
        unique_paths[0][j] = 1  
    
    for i in range(m):
        unique_paths[i][0] = 1  

    for i in range(1, m):
        for j in range(1, n):  
            unique_paths[i][j] = unique_paths[i-1][j] + unique_paths[i][j-1]
    
    return unique_paths[m-1][n-1]



m = 3
n = 7
print(uniquePaths(3,7))
    
