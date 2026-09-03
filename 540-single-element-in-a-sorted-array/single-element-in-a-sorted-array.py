class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
      
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # Make mid even so we compare pairs as (mid, mid+1)
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                # Pair is correct, single element is on the right
                left = mid + 2
            else:
                # Pair is broken, single element is on the left
                right = mid

        return nums[left]
        