def houseRob(nums):
    dp = [0 for _ in range(len(nums))]

    dp[0] = nums[0]

    dp[1] = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        dp[i] = max(nums[i], dp[i-2]+nums[i])
    return dp[-1]