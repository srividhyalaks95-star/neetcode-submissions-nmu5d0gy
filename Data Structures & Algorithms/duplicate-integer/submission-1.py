class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        set_nums = set(nums)
        if len(set_nums) != len(nums):
            return True
        else:
            return False