#brute force 


def valid(s1,s2):
    if len(s1)!=len(s2):
        return False 
    return sorted(s1)==sorted(s2)

s1="rat"
s2="tar"
print(valid(s1,s2))
     
     
from collections import Counter

def isAnagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


class Solution(object):
    def isAnagram(self, s1, s2):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        dic1={}
        dic2={}
        for i in s1:
            if i in dic1:
                dic1[i]+=1 
            else:
                dic1[i]=1 
        for i in s2:
            if i in dic2:
                dic2[i]+=1 
            else:
                dic2[i]=1  
        for i in s1:
            if i not in dic2 or dic1[i] != dic2[i]:
                return False 
        return True 
             