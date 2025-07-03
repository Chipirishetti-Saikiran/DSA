def isPowerOfTwo(self, n):
       
        if n<=0:
            return False
        if n==1:
            return True
        if n % 2 != 0:
            return False
        return self.isPowerOfTwo(n // 2)
    
    
def pwr2(n):
        while n%2==0:
            n//=2 
            if n==1:
                return True 
            else:
                return False