class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anag_dict = defaultdict(list)
        for word in strs:
            anag_dict[''.join(sorted(word))].append(word)
        return list(anag_dict.values())