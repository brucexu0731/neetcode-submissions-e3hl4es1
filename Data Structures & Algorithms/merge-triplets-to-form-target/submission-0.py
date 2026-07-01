class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # we want to find a subset of triplets where their x max, y max and z max is target
        # because if not that means when they combine it would not be target

        # brute force is to look at every subset -> 2^n

        # we basically only want to look at triplets where ai, bi, ci are <= x, y, z respectively
        # out of all those triplets, if their max a, b, c equals x, y, z, return True
        # otherwise return False

        a_max = 0
        b_max = 0
        c_max = 0
        x, y, z = target

        for a, b, c in triplets:
            if a <= x and b <= y and c <= z:
                a_max = max(a_max, a)
                b_max = max(b_max, b)
                c_max = max(c_max, c)

        return a_max == x and b_max == y and c_max == z
        