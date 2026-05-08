class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        memo = {}

        def dfs(i):
            if i == len(days):
                return 0
            if i in memo:
                return memo[i]
            
            day_pass = costs[0] + dfs(i + 1)

            week_pass = costs[1]
            j = i
            while j < len(days) and days[j] < days[i] + 7:
                j += 1
            week_pass += dfs(j)

            month_pass = costs[2]
            k = i
            while k < len(days) and days[k] < days[i] + 30:
                k += 1
            month_pass += dfs(k)

            memo[i] = min(day_pass, week_pass, month_pass)
            return memo[i]
        
        return dfs(0)
    