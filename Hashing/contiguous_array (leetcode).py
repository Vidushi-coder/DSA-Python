class Solution:
    def findMaxLength(self, nums):
        add= 0
        max_length = 0
        prefix = {0:-1}
        for i in range(len(nums)):
            if nums[i] == 0:
                add -= 1
            else:
                add += 1

            if add in prefix:
                length = i - prefix[add]
                max_length = max(length,max_length)
            else:
                prefix[add] = i

        return max_length

x = Solution()
print(x.findMaxLength([0,1,1,1,1,1,0,0,0]))