# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.
# Submit клацнул, прошло
class Solution:
    def containsDuplicate(nums) -> bool:
        if len(nums) == 1:
            return False
        new_set = set()
        new_set.add(nums[0])
        for i in range(1, len(nums)):
            if nums[i] in new_set:
                return True
            else:
                new_set.add(nums[i])
        if i + 1 == len(nums):
            return False

r = Solution
print(r.containsDuplicate([0,2,3,4]))
print(r.containsDuplicate([0]))
print(r.containsDuplicate([0,2,3,4,2]))