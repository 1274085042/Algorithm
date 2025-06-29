def longestCommonSubsequence(text1, text2):
    """
    :type text1: str
    :type text2: str
    :rtype: int
    """
    import numpy as np
    text1_len = len(text1)
    text2_len = len(text2)
    L = np.zeros((text1_len, text2_len), dtype=int)

    for i in range( text1_len):
        for j in range( text2_len):
            if text1[i] == text2[j]:
                L[i,j] = (L[i-1, j-1] if i-1>=0 and j-1>=0 else 0) + 1

            else:
                L[i,j] = max(L[i-1,j] if i-1>=0 else 0, L[i,j-1] if j-1>=0 else 0)
    
    return L[text1_len-1, text2_len-1]



text1 = "abcde"
text2 = "ace"
print(longestCommonSubsequence(text1, text2))