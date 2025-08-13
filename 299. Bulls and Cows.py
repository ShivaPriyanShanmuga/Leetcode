class Solution(object):
    def getHint(self, secret, guess):
        ctb = 0
        db = {}
        secret = list(str(secret))
        guess = list(str(guess))
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                ctb += 1
                db[i] = secret[i]
            else:
                pass
        sec = []
        gue = []
        for i in range(len(secret)):
            if i in db:
                pass
            else:
                sec.append(secret[i])
                gue.append(guess[i])
        secret = sec
        guess = gue
        guemap = {}
        for i in guess:
            if i in guemap:
                guemap[i] += 1
            else:
                guemap[i] = 1
        ctc = 0
        for i in guemap:
            ctc += min(guemap[i], secret.count(i))
        return str(ctb) + 'A' + str(ctc) + 'B'