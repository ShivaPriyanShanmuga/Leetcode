class Solution(object):
    def numberToWords(self, num):
        if num:
            hashmap_for_100_1 = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}

            hashmap_for_10 = {2:"Twenty", 3:"Thirty", 4:"Forty", 5:"Fifty", 6:"Sixty", 7:"Seventy", 8:"Eighty", 9:"Ninety"}

            hashmap_for_special_1 = {0:"Ten", 1:"Eleven", 2:"Twelve", 3:"Thirteen", 4:"Fourteen", 5:"Fifteen", 6:"Sixteen", 7:"Seventeen", 8:"Eighteen", 9:"Nineteen"}

            final = []
            def interp_100(num):
                string = []
                if num // 100:
                    string += [hashmap_for_100_1[num // 100]] + ["Hundred"]
                num = num % 100
                if num // 10 == 1:
                    string += [hashmap_for_special_1[num % 10]]
                    return string
                if num // 10:
                    string += [hashmap_for_10[num // 10]]
                num %= 10
                if num:
                    string += [hashmap_for_100_1[num % 10]]
                return string
            if num // (10 ** 9):
                final.extend(interp_100(num // (10 ** 9)) + ["Billion"])
                num %= (10 ** 9)
            if num // (10 ** 6):
                final.extend(interp_100(num // (10 ** 6)) + ["Million"])
                num %= (10 ** 6)
            if num // (1000):
                final.extend(interp_100(num // 1000) + ["Thousand"])
                num %= 1000
            final.extend(interp_100(num))
            return " ".join(final)
        else:
            return "Zero"
            