class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            if nums[pivot] == target:
                return pivot
            elif nums[pivot] > target:
                right = pivot - 1
            else:
                left = pivot + 1
        return -1


solution = Solution()
print((solution.search([-1, 0, 3, 5, 9, 12], 9)))
