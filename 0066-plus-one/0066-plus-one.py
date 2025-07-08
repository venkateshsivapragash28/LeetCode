class Solution(object):
    def plusOne(self, digits):
        num = ""
        result = []
        for i in digits:
            num = num + str(i)
        number = int(num)
        number = number+1
        string = str(number)
        for i in string:
            result.append(int(i))
        return result

        