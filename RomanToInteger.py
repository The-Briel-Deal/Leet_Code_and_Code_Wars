class Solution:
    def romanToInt(self, s: str) -> int:
        romanDict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        currentVal = 0
        previousVal = 0
        totalVal = 0
        index = 0
        size = len(s)
        while index < size:
            currentVal = romanDict[s[index]]
            index+=1
            if currentVal<=previousVal:
                totalVal += previousVal
                previousVal=currentVal
                continue
            previousVal=currentVal-previousVal
        totalVal+=previousVal
        return totalVal
        


s = Solution()
print(s.romanToInt("III"))
