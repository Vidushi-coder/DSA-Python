class Solution:
    def containsDuplicate(self,s,t):
        if sorted(s) == sorted(t):
            return True
        else:
            return False

x = Solution()
print(x.containsDuplicate("anagram","nagaram"))