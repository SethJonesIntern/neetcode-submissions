class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        smap = defaultdict(list)
        for x in strs:
            temp = "".join(sorted(x))
            smap[temp].append(x)
        return list(smap.values())
        