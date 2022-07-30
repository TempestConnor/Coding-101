nums = [7,2,2,5,7,1,3]
val = 2
try:
    while True:
        nums.remove(val)
except ValueError:
    pass
print(nums)