class Solution(object):
    def uniqueMorseRepresentations(self, words):
        hashmap = {'a': '.-', 'c': '-.-.', 'b': '-...', 'e': '.', 'd': '-..', 'g': '--.', 'f': '..-.', 'i': '..', 'h': '....', 'k': '-.-', 'j': '.---', 'm': '--', 'l': '.-..', 'o': '---', 'n': '-.', 'q': '--.-', 'p': '.--.', 's': '...', 'r': '.-.', 'u': '..-', 't': '-', 'w': '.--', 'v': '...-', 'y': '-.--', 'x': '-..-', 'z': '--..'}
        l = []
        for i in words:
            encoded = ''
            for j in i:
                encoded += hashmap[j]
            if encoded in l:
                pass
            else:
                l.append(encoded)
        return len(l)