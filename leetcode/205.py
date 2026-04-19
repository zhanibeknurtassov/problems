class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashdict = {}
        seen_t = set()

        t = list(t.encode("ascii"))
        s = list(s.encode("ascii"))

        for i in range(len(s)):
            if s[i] not in hashdict:
                if t[i] not in seen_t:
                    hashdict[s[i]] = t[i]
                    seen_t.add(t[i])
                else: return False
            else:
                if hashdict[s[i]] != t[i]:
                    return False
                
            
        for i in range(len(s)):
            s[i] = hashdict[s[i]]

        return s==t