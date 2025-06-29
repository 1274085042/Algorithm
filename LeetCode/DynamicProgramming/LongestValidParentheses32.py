def longestValidParentheses(s):
    """
    :type s: str
    :rtype: int
    """
    str_len = len(s)
    if str_len==0 or str_len==1:
        return 0
    valid_parentheses = [0] * (str_len)
    for i in range(1, str_len):  
        if s[i-1]=="(" and  s[i]==")":
            valid_parentheses[i] = (valid_parentheses[i - 2] if i-2>0 else 0) + 2
        elif s[i-1]==")" and s[i]==")":  
            if i-valid_parentheses[i-1]-1>=0 and s[i-valid_parentheses[i-1]-1]=="(" :
                valid_parentheses[i] = valid_parentheses[i-1] + 2 + (valid_parentheses[i - valid_parentheses[i-1] - 2] if  valid_parentheses[i-1] - 2>=0 else 0 )            

    return max(valid_parentheses)


# s1 = "(()"
s2 ="(()))())("
# print(longestValidParentheses(s1))
print(longestValidParentheses(s2))
