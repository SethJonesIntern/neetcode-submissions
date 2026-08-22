class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):  return False
        smap = {}
        for x in s:
            if x in smap:
                smap[x] += 1
            else: smap[x] = 1
        
        for x in t:
            if x in smap:
                smap[x] -= 1
            else: return False

        for x in smap:
            if smap[x] != 0: return False
        return True