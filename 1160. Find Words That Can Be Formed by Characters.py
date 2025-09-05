class Solution(object):
    def countCharacters(self, words, chars):
        if words == []:
            return 0
        else:
            st = words[0]
            test = True
            for i in st:
                if st.count(i) <= chars.count(i):
                    pass
                else:
                    test = False
                    break
            if test:
                return len(st) + Solution.countCharacters(self, words[1:], chars)
            else:
                return Solution.countCharacters(self, words[1:], chars)