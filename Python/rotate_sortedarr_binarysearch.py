class Solution:
    def binary_search(self,nums,target):
        start,end = 0,len(nums)-1
        while start<=end:
            middle = start + (end-start) // 2
            if nums[middle] == target:
                return middle
            elif nums[start] <= nums[middle]:
                if nums[start] <= target and target <= nums[middle]:
                    end = middle-1
                else:
                    start = middle+1
                
            elif nums[middle] <= nums[end]:
                if nums[end] >= target and target >= nums[middle]:
                    start = middle +1
                else:
                    end = middle -1
            
        return -1
    
if __name__=='__main__':
    sol = Solution()
    nums = [4,5,6,7,0,1,2]
    target =0
    print(sol.binary_search(nums,target))
