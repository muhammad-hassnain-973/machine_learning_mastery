class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_idx={}
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in num_idx:
                return num_idx[complement],i
            num_idx[nums[i]]=i