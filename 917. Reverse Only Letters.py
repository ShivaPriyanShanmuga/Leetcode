class Solution(object):
    def reverseOnlyLetters(self, s):
        st = []
        h = {}
        for i in range(len(s)):
            if s[i].isalpha():
                st.append(s[i])
            else:
                h[i] = s[i]
        st = st[::-1]
        f = ''
        for i in range(len(s)):
            if i in h:
                f += h[i]
            else:
                f += st[0]
                st.pop(0)
        return f