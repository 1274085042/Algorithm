import numpy as np

def OptimalBST(p, q, n):
    """ Construct a binary search tree whose expected search cost is smallest. 
    
    Arguments:
    p -- array of probabilities of succesful searches. 
    q -- array of probabilities of unsuccessful searches.
    n -- number of distinct keys

    Returns:
    e -- the cost of an optimal solution for keys k[i] to k[j].

    root -- the root of an optimal binary search tree for each subproblem. root[i, j]
    is the root of an optimal binary search tree containing the keys k[i]
    to k[j].
    """
    e = np.full((n, n), np.inf)
    root = np.zeros((n, n), dtype=int)

    # w = np.zeros((n, n), dtype=int)

    for l in range(1, n+1):
        
        for i in range(0, n):  
            j = i + l - 1 
            w = 0

            if j >= n :
                break

            for r in range(i, j+1):   
                w += (p[r] + q[r])
            w += q[j+1]

            for r in range(i, j+1):               
                c = (e[i, r-1] if i-1 != r-1 else q[i]) + (e[r+1, j] if r!=j else q[r+1]) + w  

                if c<e[i,j]:
                    e[i,j] = c
                    root[i,j] = r

    return e, root
              

# Testing
if __name__ == "__main__":
    # Example from textbook.
    # k is the sequence of n distinct keys in sorted order. 
    p = [0.15, 0.10, 0.05, 0.10, 0.20]  
    q = [0.05, 0.10, 0.05, 0.05, 0.05, 0.10]
    e, root = OptimalBST(p, q, len(p))
    print(e)
    print()
    print(root)
