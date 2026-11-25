class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashMap = {}
        # # Counts Each Number
        # for num in nums:
        #     hashMap[num] = hashMap.get(num, 0) + 1
        # # { num : count }


        # print(hashMap)

        # heap = [];
        # answer = []
        # for key, value in hashMap.items():
        #     heapq.heappush(heap, (-value, key))

        # print(heap)
        # for _ in range(k):
        #     answer.append(heapq.heappop(heap)[1])

        # return answer
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
