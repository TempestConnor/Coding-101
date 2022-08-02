#this one is fucked man....
nums = [1,3,5,7,9]
target = 10
try:
    for i in range(len(nums)):
        
         if nums[i] == target:
             print(i)
             break
         elif nums[i] > target:
            print(i - 1)
            break
    print(nums)
        
except:
    print("fuck")  
    