class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        #convert both strings into an array of in digits for convenience
        # [1, 1, 1]
        # [2, 2, 2]
        # [0, 0, 0, 0, 0, 0]
        n1 = []
        n2 = []

        for n in num1:
            n1.append(int(n))
        for n in num2:
            n2.append(int(n))
        
        #res is an array of the max number of digits that the result can be
        res = [0] * (len(n1) + len(n2))

        start_digit = len(res) - 1
        n2_digit = len(n2) - 1

        #do the normal long multiplication of n1 against every digit in n2
        while n2_digit >= 0:
            #each iteration we start off at the next decimal of n2 as well as res,
            # we multiply each digit of n2 through n1 and modify res[s] accordingly
            d2 = n2_digit
            d1 = len(n1) - 1
            s = start_digit
            carry_curr = 0
            carry_s = 0
            # print(d2)
            # print(s)

            while d1 >= 0 or carry_curr:
                curr = carry_curr if d1 < 0 else n1[d1] * n2[d2] + carry_curr
                # if d2 == 1:
                #     print("d1", d1)
                #     print("carry_curr", carry_curr)
                #     print("carry_s", carry_s)
                #     print("curr", curr)
                carry_curr = 0
                if curr >= 10:
                    carry_curr = curr // 10
                    curr = curr % 10 
                val_s = res[s] + curr + carry_s 
                carry_s = 0
                # if d2 == 1:
                #     print("val_s", val_s)
                #     print("s", s)
                if val_s >= 10:
                    carry_s = val_s // 10
                    val_s = val_s % 10
                res[s] = val_s
                d1 -= 1
                s -= 1
                # if d2 == 1:
                #     print(res)
            # print("carry_s", carry_s)
            # print(s)
            while carry_s:
                res[s] += carry_s
                carry_s = 0
                if res[s] >= 10:
                    carry_s = res[s] // 10
                    res[s] = res[s] % 10
                s -= 1
            #print(res)
            start_digit -= 1
            n2_digit -= 1
        
        i = 0
        while i < len(res) - 1 and res[i] == 0:
            i += 1
        res = res[i:]

        return "".join([str(n) for n in res])

                
            
            








