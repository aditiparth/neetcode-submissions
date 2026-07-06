class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numcount=Counter(nums)
        commonk=numcount.most_common(k)
        result=[item[0] for item in commonk]
        return result