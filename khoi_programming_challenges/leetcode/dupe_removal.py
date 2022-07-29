nums = [1,1,2]
output = []
k = 0
# k should be number removed,
# output should be result
for number in nums:
    if number not in output:
        output.append(number)
    else:
        k += 1
nums = output
print(nums)
