from collections import defaultdict
class UnionFind:
    def __init__(self, n):
        self.root = {}
        self.rank = {}
        for i in range(n):
            self.root[i] = i
            self.rank[i] = 0
    
    def find(self, n):
        if self.root[n] != n:
            self.root[n] = self.find(self.root[n])
        return self.root[n]
    
    def union(self, n1, n2):
        r1, r2 = self.find(n1), self.find(n2)
        if r1 == r2:
            return False 
        
        if self.rank[r1] > self.rank[r2]:
            self.root[r2] = r1
        elif self.rank[r1] < self.rank[r2]:
            self.root[r1] = r2
        else:
            self.root[r2] = r1
            self.rank[r1] += 1
        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))
        print(uf.root)

        email_to_account_number = {}
        for number, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account_number:
                    parent = email_to_account_number[email]
                    print(number, parent)
                    uf.union(number, parent)
                else:
                    email_to_account_number[email] = number

        account_emails = defaultdict(list)    
        for email, acc in email_to_account_number.items():
            root = uf.find(acc)
            account_emails[root].append(email)
        
        res = []
        for acc, emails in account_emails.items():
            res.append([accounts[acc][0]] + sorted(emails))
        
        return res


        






