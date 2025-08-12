class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st = []
        tt  = []

        for i in s:
            if st and i == '#':
                st.pop()
            else:
                st.append(i)

        for i in t:
            if tt and i == '#':
                tt.pop()
            else:
                tt.append(i)
        
        for i in st:
            if i == '#':
                st = st[1:]
        for i in tt:
            if i == '#':
                tt = tt[1:]

        if st == tt:
            return True
        else:
            return False