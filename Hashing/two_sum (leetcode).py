class Solution:
    def twoSum(self, nums, target):
        l = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                if nums[i] + nums[j] == target:
                    l.append(i)
                    l.append(j)

        return l


x = Solution()

print(x.twoSum([3, 2, 4], 6))