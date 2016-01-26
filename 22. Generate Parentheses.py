class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        self.generate(n,n,'',res)
        return res
        
    def generate(self,l,r,str,res):
        if l == 0 and r == 0:
            res.append(str)
            return
        if l > 0:
            self.generate(l-1,r,str+'(',res)
        if r>l:
            self.generate(l,r-1,str+')',res)
