# 26. Remove Duplicates from Sorted Array
class Solution:
    def removeDuplicates(self, nums) -> int:
        i,j=0,1
        ans=1
        while(j<len(nums)):
            if nums[j]==nums[i]:
                j+=1
            else:
                if j-i>1:
                    nums[i+1]=nums[j]
                ans+=1
                i+=1
                j+=1
        return ans

a = Solution()
print(a.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))