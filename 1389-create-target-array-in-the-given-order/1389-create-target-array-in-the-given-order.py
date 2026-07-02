class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for i in range(len(nums)):
            # The list.insert(index, element) method inserts the element 
            # at the specified position and shifts existing elements to the right.
            target.insert(index[i], nums[i])
        return target