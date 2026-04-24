class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [1] * (2 * len(nums))
        for i in range (len(nums)):
            ans[i] = ans[i+len(nums)] = nums[i]
        return ans
        