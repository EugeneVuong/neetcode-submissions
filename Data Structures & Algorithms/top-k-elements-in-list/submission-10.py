class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        # Counts Each Number
        for num in nums:
            hashMap[num] = hashMap.get(num, 0) + 1
        # { num : count }


        print(hashMap)

        heap = [];
        answer = []
        for key, value in hashMap.items():
            heapq.heappush(heap, (-value, key))

        print(heap)
        for _ in range(k):
            answer.append(heapq.heappop(heap)[1])

        return answer