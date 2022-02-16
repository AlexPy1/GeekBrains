# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.
def zero_out(nums):
    n = len(nums)
    j = 0
    for i in range(n):
        nums[j] = nums[i]
        j += 1 if nums[i] else 0
    nums[j:] = [0] * (n - j)
    return nums

a = [0,0,1,2,0,2,1]
b = [1,2,0,3,4,0,5,5,0,6,]
c = [1]

print(zero_out(a))
print(zero_out(b))
print(zero_out(c))
