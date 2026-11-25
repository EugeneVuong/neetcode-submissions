class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Create a Hash List
        unique_list = set()
        # Go Through The List
        for i in nums:
            # If it is in list, it is true
            if i in unique_list:
                return True
            unique_list.add(i)
        # If it is not, it is false
        return False

                
            
        