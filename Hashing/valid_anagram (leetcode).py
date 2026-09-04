class Solution:
    def validAnagram(self, s, t):
        if sorted(s) == sorted(t):
            return True
        else:
            return False

x = Solution()
print(x.validAnagram("anagram","nagaram"))