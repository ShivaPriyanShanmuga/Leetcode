class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        mag = []
        for i in magazine:
            mag.append(i)
        for i in ransomNote:
            if i in mag:
                mag.remove(i)
            else:
                return False
        return True
        