class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complements = {}
        for idx, num in enumerate(nums):
            other_num = target - num
            if other_num in complements:
                return [complements[other_num], idx]
            complements[num] = idx
            
        