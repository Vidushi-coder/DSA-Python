nums = [100,4,200,1,3,2]
num_set = set(nums)
longest = 0
for i in num_set:
    if i-1 not in num_set:
        current = i
        count = 1

        while current + 1 in num_set:
            current +=1
            count += 1

        longest = max(longest,count)

print(longest)