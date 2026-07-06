class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrammap=defaultdict(list)
        for word in strs:
            sorted_word=''.join(sorted(word))
            anagrammap[sorted_word].append(word)
        return list(anagrammap.values())