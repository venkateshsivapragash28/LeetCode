class Solution(object):
    def isPalindrome(self, s):
        s = s.strip()
        st = ''
        reverse = ''
        s = s.replace(" ","")
        for i in s:
            if i.isalnum():
                st += i
        st = st.lower()
        if st == st[::-1]:
            return True
        return False
