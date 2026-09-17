class Solution:
  def pow(self,x,n):
    if n == 0:
      return 1
    if n < 0:
      x = 1/x
      n = -n
    if n%2 == 0:
      return (self.pow(x,n//2))**2
    else:
      return x*((self.pow(x,n//2))**2)

x = Solution() 
print(x.pow(2,4))