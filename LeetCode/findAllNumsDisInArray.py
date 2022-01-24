class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        HS = set()
        for _ in range(1, len(nums)+1):
            HS.add(_)
        for _ in nums:
            HS.discard(_)
        return HS