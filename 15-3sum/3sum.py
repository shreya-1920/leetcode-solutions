class Solution:
    def threeSum(self, nums):
        ans = []

        # 1. Sort the array
        nums.sort()

        # 2. Fix one element
        for i in range(len(nums) - 2):

            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            # If nums[i] is positive, sum can never be 0
            if nums[i] > 0:
                break

            left = i + 1
            right = len(nums) - 1

            # 3. Two pointer approach
            while left < right:

                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    ans.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return ans