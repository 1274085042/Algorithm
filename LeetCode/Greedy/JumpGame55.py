def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """

    max_reach = nums[0]  
    last_pos = len(nums) -1
    for i,jump in enumerate(nums):
        if max_reach >= last_pos:
            return True
        if i<=max_reach:
            max_reach = max(i+jump, max_reach) # 贪心地更新当前最远可达位置    
    return False

# 测试用例
test_cases = [
    [2,5,0,0]      # False
]

for i, nums in enumerate(test_cases):
    print(f"=== 测试用例 {i + 1} ===")
    result = canJump(nums)
    print(f"结果: {result}")
    print("=" * 30)
    print()