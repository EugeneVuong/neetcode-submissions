import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = {} # Count the Amount of Element Per Number
        for num in nums: # Time Complexity: O(N)
            count_map[num] = count_map.get(num, 0) + 1
        
        count_list = [(-v, k) for k, v in count_map.items()] # O(N)
        heapq.heapify(count_list) # O(N) Heapify
        result = []
        for _ in range(k):
            result.append(heapq.heappop(count_list)[1])
        return result


         
        