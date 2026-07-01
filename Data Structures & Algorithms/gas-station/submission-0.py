class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # compute the +- in gas at each gas station
        # [-1, 0, -1, 3]
        # prefix [-1, -1, -2, 1]
        # postfix[1, 2, 2, 3]


        # it's kind of like kadane's, where we want to keep a running sum,
        # when the sum dips below zero, we want to restart at the next station
        # because anything up to that current station won't work 
        # so similar to kadane's the running sum is the maximum number of gas we 
        
        if sum(gas) < sum(cost):
            return -1

        diff = [(gas[i] - cost[i]) for i in range(len(gas))]

        running_sum = 0
        sum_start = 0

        for i in range(len(gas)):
            running_sum += diff[i]
            if running_sum < 0:
                running_sum = 0
                sum_start = i + 1
        
        return sum_start
