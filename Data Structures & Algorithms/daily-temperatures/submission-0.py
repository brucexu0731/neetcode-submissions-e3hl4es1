class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        for i in range(len(temperatures) - 2, - 1, - 1):
            if temperatures[i] < temperatures[i + 1]:
                res[i] = 1
                continue

            days = 0
            j = i + 1
            while temperatures[i] >= temperatures[j]:
                if res[j] == 0:
                    days = -1
                    break 
                days += res[j]
                j += res[j]
            res[i] = days + 1
            

        return res 