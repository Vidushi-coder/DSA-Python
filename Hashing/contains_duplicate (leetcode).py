class Solution:
    def containsDuplicate(self, nums):
        newSet=set()
        for i in nums:
            if i in newSet:
                return True
            else:
                newSet.add(i)
        return False

x = Solution()
print(x.containsDuplicate([1,2,3,4]))