# Bruteforce - Nguyen Dinh Khoi 
# https://leetcode.com/problems/two-sum/

nums = [3,2,3]
target = 6
output =[]
for i in range(len(nums) - 1):
    for j in range(i,len(nums)):
        test = nums[i] + nums[j]
        if test == target:
            output = [i,j]
print(output)