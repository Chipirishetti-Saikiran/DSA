class solution:
    def getDominants(self,arr):
        #Write your code here...
        res=[]
        maxi=float("-inf")
        for i in reversed(arr):
            if i>=maxi:
                res.append(i)
                maxi=i 
        return res[::-1]
        
    