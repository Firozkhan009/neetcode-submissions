class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        there=set()
        for num in nums:
            if num in there:
                return True
            there.add(num)
        return False
        