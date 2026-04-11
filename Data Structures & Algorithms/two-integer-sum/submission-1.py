class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_dict = {}
        for ind, val in enumerate(nums):
            diff = target - val
            if diff in seen_dict:
                return [seen_dict[diff], ind]
            seen_dict[val] = ind