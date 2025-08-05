class Solution(object):
    def isNumber(self, s):
        l = ["inf", "-inf", "+inf", "Infinity", "-Infinity", "+Infinity", "nan"]
        if s in l:
            return False
        else:
            try:
                float(s)
                return True
            except:
                return False