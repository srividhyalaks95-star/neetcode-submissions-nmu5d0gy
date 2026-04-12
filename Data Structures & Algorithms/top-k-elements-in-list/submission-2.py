from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #freq = []
        #freq_dict = Counter(nums)
        #sorted_frq_dict = dict(sorted(freq_dict.items(), key=lambda x:x[1], reverse = True))
        #return list(sorted_frq_dict.keys())[:k]
        count = {}
        for ele in nums:
            count[ele] = 1 + count.get(ele, 0)
        
        arr = []
        for num, cnt in count.items():
            arr.append([cnt, num])
        arr.sort()

        res = []
        while len(res)<k:
            res.append(arr.pop()[1])
        return res

        