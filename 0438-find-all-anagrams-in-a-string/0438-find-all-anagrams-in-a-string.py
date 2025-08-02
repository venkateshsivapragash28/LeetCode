class Solution(object):
    def findAnagrams(self, string, p):
        # 1st Try ---------- 02 - 08 - 2025 -----------------
        # k = len(p)
        # p = sorted(p)
        # res = []
        # for i in range(len(string)-k+1):
        #     if sorted(string[i:i+k]) == p:
        #         res.append(i)
        
        # return res
        
        #2nd Try -----------------------02 - 08 - 2025-----------------------
        # k = len(p)
        # p_count = Counter(p)
        # res = []
        # for i in range(len(string)-k+1):
        #     window = sorted(string[i:i+k]) 
        #     window_count = Counter(window)
        #     if window_count == p_count:
        #         res.append(i)
        
        # return res

        #3rd Try ---------------------- 02 - 08 - 2025 -----------------------

        k = len(p)
        res = []
        p_count = Counter(p)
        window_count = Counter(string[0:k])
        if window_count == p_count:
            res.append(0)
        for i in range(1,len(string)-k+1):
            window_count[string[i-1]]  = window_count[string[i-1]] - 1
            if window_count[string[i-1]] == 0:
                del window_count[string[i-1]]
            window_count[string[i+k-1]] = window_count[string[i+k-1]] + 1

            if window_count == p_count:
                res.append(i)
        
        return res