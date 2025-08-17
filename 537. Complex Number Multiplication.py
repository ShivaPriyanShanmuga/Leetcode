class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        num1 = num1.split("+")
        num2 = num2.split("+")
        num1[1] = num1[1][:len(num1[1]) - 1]
        num2[1] = num2[1][:len(num2[1]) - 1]
        ans = [0, 0]
        for i in range(2):
            num1[i] = int(num1[i])
            num2[i] = int(num2[i])
        ans[0] = str(num1[0] * num2[0] - num1[1] * num2[1])
        ans[1] = num1[0] * num2[1] + num1[1] * num2[0]
        ans[1] = str(ans[1]) + 'i'
        return "+".join(ans)