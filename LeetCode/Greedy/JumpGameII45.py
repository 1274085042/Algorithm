def jump(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    cur_end = 0     # 当前跳的边界
    max_reach = 0   # 下一跳最远可达位置
    step = 0
    l = len(nums)

    for i in range(l-1):
        max_reach = max(i+nums[i], max_reach)  # 贪心地更新下一跳最远可达位置
        if i==cur_end:
            step += 1 
            cur_end = max_reach
    return step

# 测试用例
test_cases = [
    [0],     # 2 jumps
    [2, 1],     # 2 jumps  
    [1, 1, 1, 1],        # 3 jumps
    [1, 2, 3],           # 2 jumps
    [5, 6, 4, 4, 6, 9, 4, 4, 7, 4, 4, 8, 2, 6, 8, 1, 5, 9, 6, 5, 2, 7, 9, 7, 9, 6, 9, 4, 1, 6, 8, 8, 4, 4, 2, 0, 3, 8, 5]  # 复杂案例
]

for i, nums in enumerate(test_cases[:2]):  # 只展示前两个案例
    print(f"=== 测试用例 {i + 1} ===")
    result = jump(nums)
    print(f"最小跳跃次数: {result}")
    print("=" * 40)
    print()