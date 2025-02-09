class Solution:
    def countBadPairs(self, nums):
        n = len(nums)
        diff = [nums[i] - i for i in range(n)]
        diff.sort()
        good = 0
        count = 1
        for i in range(1, n):
            if diff[i] == diff[i - 1]:
                count += 1
            else:
                good += count * (count - 1) // 2
                count = 1
        good += count * (count - 1) // 2
        return n * (n - 1) // 2 - good