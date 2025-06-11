class Solution(object):
    def finalPositionOfSnake(self, n, commands):
        """
        :type n: int
        :type commands: List[str]
        :rtype: int
        """
        i,j=0,0 
        for a in commands:
            if a=="UP":
                i-=1
            elif a=="DOWN":
                i+=1 
            elif a=="RIGHT":
                j+=1 
            elif a=="LEFT":
                j-=1 
        val=(i * n) + j 
        return val                   
